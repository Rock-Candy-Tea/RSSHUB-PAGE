
---
title: 'Qt for Android（十二） —— QT for Android QMediaPlayer JNI交互原理和源码分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5950'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 00:19:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=5950'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">背景</h4>
<p>  本文旨在对qml的mediaplayer和android的mediaplayer是怎样交互的，qml mediaplayer的play、pause等函数是这样向下传递的，和android mediaplayer的回调函数是怎样响应到qml的槽函数的进行简要的分析和梳理，以便于对这块的内容有一个大概的了解，并清楚原理。建议下载qt5.15的源码，用source insight阅读。</p>
<h4 data-id="heading-1">源码流程（QT端）</h4>
<p>1、首先我们在QML中使用MediaPlayer组件，并设置了相关属性，增加了play、pause方法，覆盖了onplaying、onStatusChanged。如下代码：</p>
<pre><code class="copyable"> MediaPlayer &#123;
        id: player
        source: url
        autoLoad: true
        autoPlay: false
        loops: 0
        volume: ivolume
        onPlaying: &#123;
            console.log("MediaPlayer onPlaying")
        &#125;
        onError: &#123;
            if (MediaPlayer.NoError != error) &#123;
                console.log("[qmlvideo]  error " + player.error
                            + " errorString " + player.errorString)
            &#125;
        &#125;

        onStatusChanged: &#123;
            console.log("onStatusChanged" + status)
            &#125;
    &#125;
    
     function play() &#123;
       player.play()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>QML 中的MediaPlayer其实就是QT中的QMediaPlayer(<code>D:\WorkSoftware\Qt5.15.2\5.15.2\Src\qtmultimedia\src\multimedia\playback\qmediaplayer.cpp</code>)，看下构造函数：</p>
<pre><code class="copyable">QMediaPlayer::QMediaPlayer(QObject *parent, QMediaPlayer::Flags flags):
    QMediaObject(*new QMediaPlayerPrivate,
                 parent,
                 playerService(flags))
&#123;
    Q_D(QMediaPlayer);

    d->provider = QMediaServiceProvider::defaultServiceProvider();
    if (d->service == nullptr) &#123;
        d->error = ServiceMissingError;
    &#125; else &#123;
        d->control = qobject_cast<QMediaPlayerControl*>(d->service->requestControl(QMediaPlayerControl_iid));
#ifndef QT_NO_BEARERMANAGEMENT
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
        d->networkAccessControl = qobject_cast<QMediaNetworkAccessControl*>(d->service->requestControl(QMediaNetworkAccessControl_iid));
QT_WARNING_POP
#endif
        if (d->control != nullptr) &#123;
        connect(d->control, SIGNAL(mediaChanged(QMediaContent)), SLOT(_q_handleMediaChanged(QMediaContent)));
            connect(d->control, SIGNAL(stateChanged(QMediaPlayer::State)), SLOT(_q_stateChanged(QMediaPlayer::State)));
            connect(d->control, SIGNAL(mediaStatusChanged(QMediaPlayer::MediaStatus)),
                    SLOT(_q_mediaStatusChanged(QMediaPlayer::MediaStatus)));
            connect(d->control, SIGNAL(error(int,QString)), SLOT(_q_error(int,QString)));

             connect(d->control, &QMediaPlayerControl::durationChanged, this, &QMediaPlayer::durationChanged);
            connect(d->control, &QMediaPlayerControl::positionChanged, this, &QMediaPlayer::positionChanged);
            connect(d->control, &QMediaPlayerControl::audioAvailableChanged, this, &QMediaPlayer::audioAvailableChanged);
            connect(d->control, &QMediaPlayerControl::videoAvailableChanged, this, &QMediaPlayer::videoAvailableChanged);
            connect(d->control, &QMediaPlayerControl::volumeChanged, this, &QMediaPlayer::volumeChanged);
            connect(d->control, &QMediaPlayerControl::mutedChanged, this, &QMediaPlayer::mutedChanged);
            connect(d->control, &QMediaPlayerControl::seekableChanged, this, &QMediaPlayer::seekableChanged);
            connect(d->control, &QMediaPlayerControl::playbackRateChanged, this, &QMediaPlayer::playbackRateChanged);
            connect(d->control, &QMediaPlayerControl::bufferStatusChanged, this, &QMediaPlayer::bufferStatusChanged);

            d->state = d->control->state();
            d->status = d->control->mediaStatus();
            ......
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里我们只需要关注下d->control对象和其绑定的信号槽。此处调用了 d 指针的control对象，d 指针是QMediaPlayerPrivate对象，QT为了实现库的二进制兼容性，将类属性和方法实现通过私有指针的方式放到了源文件中，这样就屏蔽了实现细节和接口变动(具体可以google QT之d、p指针)。</p>
<p>2、然后qt到Android的流程跟踪以play方法为例。</p>
<pre><code class="copyable">void QMediaPlayer::play()
&#123;
    Q_D(QMediaPlayer);

    if (d->control == nullptr) &#123;
        QMetaObject::invokeMethod(this, "_q_error", Qt::QueuedConnection,
                                    Q_ARG(int, QMediaPlayer::ServiceMissingError),
                                    Q_ARG(QString, tr("The QMediaPlayer object does not have a valid service")));
        return;
    &#125;

    ......
    d->control->play();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到会调用这个d指针的control对象的play方法。所以我们先看下QMediaPlayerPrivate这个私有指针类：</p>
<pre><code class="copyable">class QMediaPlayerPrivate : public QMediaObjectPrivate
&#123;
    Q_DECLARE_NON_CONST_PUBLIC(QMediaPlayer)

public:
    QMediaPlayerPrivate()
        : provider(nullptr)
        , control(nullptr)
        , audioRoleControl(nullptr)
        , customAudioRoleControl(nullptr)
        , playlist(nullptr)
#ifndef QT_NO_BEARERMANAGEMENT
        , networkAccessControl(nullptr)
#endif
        , state(QMediaPlayer::StoppedState)
        , status(QMediaPlayer::UnknownMediaStatus)
        &#123;&#125;
            QVideoSurfaceOutput surfaceOutput;
    QMediaContent qrcMedia;
    QScopedPointer<QFile> qrcFile;

    QMediaContent rootMedia;
    QMediaContent pendingPlaylist;
    QMediaPlayer::State state;
    QMediaPlayer::MediaStatus status;
    QMediaPlayer::Error error;
    int ignoreNextStatusChange;
    int nestedPlaylists;
    bool hasStreamPlaybackFeature;

    QMediaPlaylist *parentPlaylist(QMediaPlaylist *pls);
    bool isInChain(const QUrl &url);

    void setMedia(const QMediaContent &media, QIODevice *stream = nullptr);

    void setPlaylist(QMediaPlaylist *playlist);
    void setPlaylistMedia();
    void loadPlaylist();
    void disconnectPlaylist();
    void connectPlaylist();

    void _q_stateChanged(QMediaPlayer::State state);
    void _q_mediaStatusChanged(QMediaPlayer::MediaStatus status);
    void _q_error(int error, const QString &errorString);
    ......
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到其中有个control对象，这便是我们上边看到的d->control。control类位于<code>D:\WorkSoftware\Qt5.15.2\5.15.2\Src\qtmultimedia\src\plugins\android\src\mediaplayer\qandroidmediaplayercontrol.cpp</code>路径下，顾名思义，它的意思是Android MediaPlayer的控制类。看下构造函数，并跟踪下它的play方法：</p>
<pre><code class="copyable">QAndroidMediaPlayerControl::QAndroidMediaPlayerControl(QObject *parent)
    : QMediaPlayerControl(parent),
      mMediaPlayer(new AndroidMediaPlayer),
      mCurrentState(QMediaPlayer::StoppedState),
      mCurrentMediaStatus(QMediaPlayer::NoMedia),
      mMediaStream(0),
      mVideoOutput(0),
      mSeekable(true),
      mBufferPercent(-1),
      mBufferFilled(false),
      mAudioAvailable(false),
      mVideoAvailable(false),
      mBuffering(false),
mState(AndroidMediaPlayer::Uninitialized),
      mPendingState(-1),
      mPendingPosition(-1),
      mPendingSetMedia(false),
      mPendingVolume(-1),
      mPendingMute(-1),
      mReloadingMedia(false),
      mActiveStateChangeNotifiers(0),
      mPendingPlaybackRate(1.0),
      mHasPendingPlaybackRate(false)
      &#123;
    connect(mMediaPlayer,SIGNAL(bufferingChanged(qint32)),
            this,SLOT(onBufferingChanged(qint32)));
    connect(mMediaPlayer,SIGNAL(info(qint32,qint32)),
            this,SLOT(onInfo(qint32,qint32)));
    connect(mMediaPlayer,SIGNAL(error(qint32,qint32)),
            this,SLOT(onError(qint32,qint32)));
    connect(mMediaPlayer,SIGNAL(stateChanged(qint32)),
            this,SLOT(onStateChanged(qint32)));
    connect(mMediaPlayer,SIGNAL(videoSizeChanged(qint32,qint32)),
    
  ...............................................
    
    void QAndroidMediaPlayerControl::play()
&#123;
    StateChangeNotifier notifier(this);

    // We need to prepare the mediaplayer again.
    if ((mState & AndroidMediaPlayer::Stopped) && !mMediaContent.isNull()) &#123;
        setMedia(mMediaContent, mMediaStream);
    &#125;

    if (!mMediaContent.isNull())
        setState(QMediaPlayer::PlayingState);

   
    if ((mState & (AndroidMediaPlayer::Prepared
                   | AndroidMediaPlayer::Started
                   | AndroidMediaPlayer::Paused
                   | AndroidMediaPlayer::PlaybackCompleted)) == 0) &#123;
        mPendingState = QMediaPlayer::PlayingState;
        return;
    &#125;

    mMediaPlayer->play();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中，其一是绑定了一个AndroidMediaPlayer到Control类的信号槽，其二从<code>setState</code>函数可以看到，在Control类中维护了一套AndroidMediaPlayer的播放状态。</p>
<p>这个类中还有个有趣的东西，即<code>StateChangeNotifier notifier(this);</code>这句代码，其实就是借助了类的构造和退栈析构，在其中搞事情，可以顺便看下：</p>
<pre><code class="copyable">class StateChangeNotifier
&#123;
public:
    StateChangeNotifier(QAndroidMediaPlayerControl *mp)
        : mControl(mp)
        , mPreviousState(mp->state())
        , mPreviousMediaStatus(mp->mediaStatus())
    &#123;
        ++mControl->mActiveStateChangeNotifiers;
    &#125;

    ~StateChangeNotifier()
    &#123;
        if (--mControl->mActiveStateChangeNotifiers)
            return;

       if (mPreviousMediaStatus != mControl->mediaStatus())
            Q_EMIT mControl->mediaStatusChanged(mControl->mediaStatus());

        if (mPreviousState != mControl->state())
            Q_EMIT mControl->stateChanged(mControl->state());
    &#125;

private:
    QAndroidMediaPlayerControl *mControl;
    QMediaPlayer::State mPreviousState;
    QMediaPlayer::MediaStatus mPreviousMediaStatus;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>他的意思是用析构时的state和构造时的state作比较，如果发生了改变就会在析构的时候调用<code>Q_EMIT stateChanged</code>更新播放器的状态，这个信号在最开始的QMediaPlayer的构造函数中见过，最终状态的更新会发送到QMediaPlayer中，最终也就会发送到QML层。</p>
<p>3、继续来跟踪play方法，在control类中调用了<code>mMediaPlayer->play();</code>，mMediaPlayer是一个AndroidMediaPlayer对象，所以进入到AndroidMediaPlayer类（位于<code>D:\WorkSoftware\Qt5.15.2\5.15.2\Src\qtmultimedia\src\plugins\android\src\wrappers\jni\androidmediaplayer.cpp</code>路径下）：</p>
<pre><code class="copyable">static const char QtAndroidMediaPlayerClassName[] = "org/qtproject/qt5/android/multimedia/QtAndroidMediaPlayer";
typedef QVector<AndroidMediaPlayer *> MediaPlayerList;
Q_GLOBAL_STATIC(MediaPlayerList, mediaPlayers)
Q_GLOBAL_STATIC(QReadWriteLock, rwLock)

QT_BEGIN_NAMESPACE

AndroidMediaPlayer::AndroidMediaPlayer()
    : QObject()
&#123;
    QWriteLocker locker(rwLock);
    auto context = QtAndroidPrivate::activity() ? QtAndroidPrivate::activity() : QtAndroidPrivate::service();
    const jlong id = reinterpret_cast<jlong>(this);
    mMediaPlayer = QJNIObjectPrivate(QtAndroidMediaPlayerClassName,
                                     "(Landroid/content/Context;J)V",
                                     context,
                                     id);
    mediaPlayers->append(this);
&#125;

AndroidMediaPlayer::~AndroidMediaPlayer()
&#123;
    QWriteLocker locker(rwLock);
    const int i = mediaPlayers->indexOf(this);
    Q_ASSERT(i != -1);
    mediaPlayers->remove(i);
&#125;

void AndroidMediaPlayer::play()
&#123;
    mMediaPlayer.callMethod<void>("start");
&#125;

static void onStateChangedNative(JNIEnv *env, jobject thiz, jint state, jlong id)
&#123;
    Q_UNUSED(env);
    Q_UNUSED(thiz);
    QReadLocker locker(rwLock);
    const int i = mediaPlayers->indexOf(reinterpret_cast<AndroidMediaPlayer *>(id));
    if (Q_UNLIKELY(i == -1))
        return;

    Q_EMIT (*mediaPlayers)[i]->stateChanged(state);
&#125;

bool AndroidMediaPlayer::initJNI(JNIEnv *env)
&#123;
    jclass clazz = QJNIEnvironmentPrivate::findClass(QtAndroidMediaPlayerClassName,
                                                     env);

    static const JNINativeMethod methods[] = &#123;
        &#123;"onErrorNative", "(IIJ)V", reinterpret_cast<void *>(onErrorNative)&#125;,
        &#123;"onBufferingUpdateNative", "(IJ)V", reinterpret_cast<void *>(onBufferingUpdateNative)&#125;,
        &#123;"onProgressUpdateNative", "(IJ)V", reinterpret_cast<void *>(onProgressUpdateNative)&#125;,
        &#123;"onDurationChangedNative", "(IJ)V", reinterpret_cast<void *>(onDurationChangedNative)&#125;,
        &#123;"onInfoNative", "(IIJ)V", reinterpret_cast<void *>(onInfoNative)&#125;,
        &#123;"onVideoSizeChangedNative", "(IIJ)V", reinterpret_cast<void *>(onVideoSizeChangedNative)&#125;,
        &#123;"onStateChangedNative", "(IJ)V", reinterpret_cast<void *>(onStateChangedNative)&#125;
   &#125;;

    if (clazz && env->RegisterNatives(clazz,
                                      methods,
                                      sizeof(methods) / sizeof(methods[0])) != JNI_OK) &#123;
            return false;
    &#125;
    return true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到AndroidMediaPlayer类中也有一个mMediaPlayer对象，这是一个QJNIObjectPrivate对象，代表了一个JNI对象。从构造函数中可以看到它指的是<code>org/qtproject/qt5/android/multimedia/QtAndroidMediaPlayer</code>这个Java类，一会儿再看QtAndroidMediaPlayer类。</p>
<p>第一：可以看到play方法的调用最终是通过JNI调用Java类的start函数。到这儿就知道了QT的play方法怎么调到Android端。</p>
<p>第二：从上面第二行和第三行先看下这个静态的MediaPlayerList，它将AndroidMediaPlayer指针缓存到一个vector中。以onStateChangedNative函数为例，这是一个native函数，会被Java层调用。当收到Android端的onStateChanged时触发。所以上面构造函数中的ID会先传递到Android层，然后在收到native调用后再传回来，根据ID找到对应的AndroidMediaPlayer对象。结合上面第2步末尾的信号槽和这儿的信号槽也就知道了Android端的回调怎么传递到QT中乃至于QML中。</p>
<h4 data-id="heading-2">源码流程（Android端）</h4>
<p>Android端的代码时位于jar包中的，位于<code>D:\WorkSoftware\Qt5.15.2\5.15.2\android\jar</code>路径下。</p>
<p>简单看下它的成员对象和一些重要的方法：</p>
<pre><code class="copyable">public class QtAndroidMediaPlayer
&#123;
    // Native callback functions for MediaPlayer
    native public void onErrorNative(int what, int extra, long id);
    native public void onBufferingUpdateNative(int percent, long id);
    native public void onProgressUpdateNative(int progress, long id);
    native public void onDurationChangedNative(int duration, long id);
    native public void onInfoNative(int what, int extra, long id);
    native public void onVideoSizeChangedNative(int width, int height, long id);
    native public void onStateChangedNative(int state, long id);

    private MediaPlayer mMediaPlayer = null;
    private AudioAttributes mAudioAttributes = null;
    private HashMap<String, String> mHeaders = null;
    private Uri mUri = null;
    private final long mID;
    
        public QtAndroidMediaPlayer(final Context context, final long id)
    &#123;
        mID = id;
        mContext = context;
    &#125;
    
        private class MediaPlayerCompletionListener
            implements MediaPlayer.OnCompletionListener
    &#123;
        @Override
        public void onCompletion(final MediaPlayer mp)
        &#123;
            Log.d( TAG,"onCompletion mMediaPlayer.release()");
            setState(org.qtproject.qt5.android.multimedia.QtAndroidMediaPlayer.State.PlaybackCompleted);
        &#125;
    &#125;
    
        private void setState(int state)
    &#123;
        if (mState == state)
            return;

        mState = state;

        onStateChangedNative(mState, mID);
    &#125;
    
        public void start()
    &#123;
        if ((mState & (org.qtproject.qt5.android.multimedia.QtAndroidMediaPlayer.State.Prepared
                | org.qtproject.qt5.android.multimedia.QtAndroidMediaPlayer.State.Started
                | org.qtproject.qt5.android.multimedia.QtAndroidMediaPlayer.State.Paused
                | org.qtproject.qt5.android.multimedia.QtAndroidMediaPlayer.State.PlaybackCompleted)) == 0) &#123;
            return;
        &#125;
        try &#123;
            mMediaPlayer.start()
                        setState(org.qtproject.qt5.android.multimedia.QtAndroidMediaPlayer.State.Started);
            Log.d(TAG, "start");
        &#125; catch (final IllegalStateException e) &#123;
            Log.d(TAG, "" + e.getMessage());
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中我们能看到几个东西：<br>
第一：如上面说的QT端和Android端均维护了一套状态。<br>
第二：执行完start方法后会setState，setState会调用native函数onStateChangedNative，其实基本上每个函数都会setState，一是更新这边的状态，二是调用QT库的native函数，更新Control类里面的状态。</p>
<p>正常来说，jar包的代码是不允许更改的，但是为了一些定制功能，我们也可以去修改。但是此时我们不需要改jar包，因QT为源码中包含了这个jar包代码，在<code>\5.15.2\Src\qtmultimedia\src\plugins\android\jar\src\org\qtproject\qt5\android\multimedia</code>这个路径下，可以直接拿过来加到项目中使用。</p></div>  
</div>
            