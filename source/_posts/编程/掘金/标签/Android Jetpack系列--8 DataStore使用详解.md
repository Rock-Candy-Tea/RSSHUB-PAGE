
---
title: 'Android Jetpack系列--8. DataStore使用详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8184'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 18:50:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=8184'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">SharedPreferences 和 DataStore 对比</h3>
<h4 data-id="heading-1">SharedPreferences：</h4>
<ol>
<li>可能阻塞UI线程，导致ANR异常（需要等等sp文件加载完成，而且存储数据越多，文件越大，加载越慢，所有我们之前使用时都会分类存储在不同的sp文件中，如用户信息，业务信息，统计信息等）且不能用于跨进程通信</li>
</ol>
<pre><code class="copyable">// ContextImpl.getSharedPreferences()
public SharedPreferences getSharedPreferences(File file, int mode) &#123;
    SharedPreferencesImpl sp;
    synchronized (ContextImpl.class) &#123;
        final ArrayMap<File, SharedPreferencesImpl> cache = getSharedPreferencesCacheLocked();
        sp = cache.get(file);
        if (sp == null) &#123;
            ...
            sp = new SharedPreferencesImpl(file, mode);
            cache.put(file, sp);
            return sp;
        &#125;
    &#125;
    //MODE_MULTI_PROCESS只是重新加载一下sp，并不能保证跨进程安全的
    if ((mode & Context.MODE_MULTI_PROCESS) != 0 ||
        getApplicationInfo().targetSdkVersion < android.os.Build.VERSION_CODES.HONEYCOMB) &#123;
        // If somebody else (some other process) changed the prefs
        // file behind our back, we reload it.  This has been the
        // historical (if undocumented) behavior.
        sp.startReloadIfChangedUnexpectedly();
    &#125;
    return sp;
&#125;
//1. SharedPreferences对象的创建会开启异步线程读取数据
//SharedPreferencesImpl.startLoadFromDisk()
private void startLoadFromDisk() &#123;
    synchronized (mLock) &#123;
        mLoaded = false;
    &#125;
    new Thread("SharedPreferencesImpl-load") &#123;
        public void run() &#123;
            loadFromDisk();
        &#125;
    &#125;.start();
&#125;

//2. SharedPreferences.getXX()是同步的，会调用wait方法等待对象加载完毕,就可能导致ANR
public String getString(String key, @Nullable String defValue) &#123;
    synchronized (mLock) &#123;
        awaitLoadedLocked();
        String v = (String)mMap.get(key);
        return v != null ? v : defValue;
    &#125;
&#125;
//3. SharedPreferences.apply()是异步的，但是当生命周期处于handleStopService()，handlePauseActivity(),
//handleStopActivity() 时, 会一直等待apply()方法将数据保存成功，否则会一直等待，就可能导致ANR;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>加载的数据会一直留在内存中，浪费内存</li>
</ol>
<pre><code class="copyable">// 使用静态的ArrayMap缓存每个SP文件,在ContextImpl.getSharedPreferences()中调用
private static ArrayMap<String, ArrayMap<File, SharedPreferencesImpl>> sSharedPrefsCache;
private ArrayMap<File, SharedPreferencesImpl> getSharedPreferencesCacheLocked() &#123;
    if (sSharedPrefsCache == null) &#123;
        sSharedPrefsCache = new ArrayMap<>();
    &#125;

    final String packageName = getPackageName();
    ArrayMap<File, SharedPreferencesImpl> packagePrefs = sSharedPrefsCache.get(packageName);
    if (packagePrefs == null) &#123;
        packagePrefs = new ArrayMap<>();
        sSharedPrefsCache.put(packageName, packagePrefs);
    &#125;

    return packagePrefs;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>非类型安全的，可能导致ClassCastException异常；</li>
</ol>
<pre><code class="copyable">val sp=getSharedPreferences("ljy.sp",Context.MODE_PRIVATE)
//sp.edit默认是apply，可以手动设置为commit
//apply:提交会先写入内存，然后异步写入磁盘
//commit:直接写入磁盘
//如果频繁操作的话 apply 的性能会优于 commit
//提交数据时， 尽量使用apply,而非commit，仅当需要确定提交结果，并据此有后续操作时，使用commit;
sp.edit(commit = true) &#123;
    putString("name", "洋仔")
    putInt("age", 17)
&#125;
val name=sp.getBoolean("name",false)
val age=sp.getInt("age",false)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>apply() 方法无法获取到操作成功或者失败的结果</li>
</ol>
<h4 data-id="heading-2">DataStore</h4>
<ul>
<li>旨在替代原有的 SharedPreferences，支持SharedPreferences数据的迁移</li>
<li>基于 Kotlin 协程和 Flow 开发,保证了在主线程的安全性</li>
<li>提供两种不同的实现:
<ul>
<li>Preferences DataStore：使用键存储和访问数据。</li>
<li>Proto DataStore： 将数据作为自定义数据类型的实例进行存储。</li>
</ul>
</li>
<li>以事务方式处理更新数据，事务有四大特性（原子性、一致性、 隔离性、持久性）</li>
<li>如果需要支持大型或复杂数据集、部分更新或参照完整性，请考虑使用 Room，而不是 DataStore。</li>
</ul>
<h5 data-id="heading-3">Preferences DataStore 与 Proto DataStore 区别</h5>
<ol>
<li>Preferences DataStore 根据键访问xml文件存储的数据，无需事先定义架构,解决了sp的不足；</li>
<li>Proto DataStore 使用协议缓冲区（protocol buffers）来定义架构，可持久保留强类型数据（可以确保类型安全），与xml存储相比协议缓冲区速度更快、规格更小、使用更简单，并且更清楚明了，但需要学习新的序列化机制；</li>
</ol>
<h3 data-id="heading-4">DataStore的使用</h3>
<h4 data-id="heading-5">使用 Preferences DataStore 存储键值对</h4>
<h5 data-id="heading-6">添加依赖</h5>
<pre><code class="copyable">//(1) Datastore Preferences
implementation "androidx.datastore:datastore-preferences:1.0.0-alpha08"
// optional - RxJava2 support
implementation("androidx.datastore:datastore-preferences-rxjava2:1.0.0-rc02")
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">创建一个常量类</h5>
<ul>
<li>便于管理文件名及键值对的key</li>
</ul>
<pre><code class="copyable">object Constants &#123;
    //SharedPreferences文件名
    const val MY_SP = "mySP"

    //DataStore<Preferences>文件名
    const val MY_PREFERENCES = "myPreferences"

    //SharedPreferences 迁移到 DataStore<Preferences> 后的文件名
    const val SP_2_PREFERENCES = "sp2Preferences"

    //SharedPreferences中的key
    const val KEY_NAME_SP = "name"

    //SharedPreferences 迁移到 DataStore<Preferences> 后的key
    val KEY_NAME = stringPreferencesKey(KEY_NAME_SP)

    //DataStore<Preferences> 中的key
    val KEY_USER_NAME = stringPreferencesKey("userName")
    val KEY_USER_AGE = intPreferencesKey("userAge")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">创建 Preferences DataStore</h5>
<ul>
<li>在Kotlin 文件顶层调用该实例一次，便可在应用的所有其余部分通过此属性访问该实例。这样可以更轻松地将 DataStore 保留为单例</li>
</ul>
<pre><code class="copyable">val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = Constants.MY_PREFERENCES)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">数据的读写和清除</h5>
<pre><code class="copyable">//1. 存储键值对数据
dataStore.edit &#123;
    it[Constants.KEY_USER_NAME] = "jinYang"
    it[Constants.KEY_USER_AGE] = 18
&#125;

//2. 读取键值对数据
dataStore.data.collect &#123;
    LjyLogUtil.d("userName:$&#123;it[Constants.KEY_USER_NAME]&#125;")
    LjyLogUtil.d("userAge:$&#123;it[Constants.KEY_USER_AGE]&#125;")
    LjyLogUtil.d("$Constants.KEY_NAME:$&#123;it[Constants.KEY_NAME]&#125;")
    LjyLogUtil.d("it:$it")
&#125;
//或者使用LiveData
dataStore.data.asLiveData().observe(this,)&#123;
    LjyLogUtil.d("asLiveData：userName:$&#123;it[Constants.KEY_USER_NAME]&#125;")
    LjyLogUtil.d("asLiveData：userAge:$&#123;it[Constants.KEY_USER_AGE]&#125;")
    LjyLogUtil.d("asLiveData：it:$it")
&#125;

//3. 清除数据
dataStore.edit &#123;
    it.clear()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">迁移 SharedPreferences 到 Preferences DataStore</h5>
<pre><code class="copyable">//1. 构建DataStore时，produceMigrations参数传入一个SharedPreferencesMigration的集合，
// 即可把多个sp文件关联到DataStore
val Context.dataStore2 by preferencesDataStore(
    name = Constants.SP_2_PREFERENCES,
    produceMigrations = &#123; context ->
        // Since we're migrating from SharedPreferences, add a migration based on the
        // SharedPreferences name
        listOf(SharedPreferencesMigration(context, Constants.MY_SP))
    &#125;
)

//2. 需要执行一次读/写操作才能完成迁移，迁移成功后会自动删除sp文件，
// 需要注意的是迁移工作只执行一次，迁移成功后需要停止再使用sp
dataStore2.data.collect &#123;
    LjyLogUtil.d("it:$it")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">使用 Proto DataStore 存储类型化的对象</h4>
<ul>
<li>SharedPreferences 和 Preferences DataStore 的一个缺点是无法定义架构，保证不了存取键时使用了正确的数据类型。</li>
<li>Proto DataStore 可利用协议缓冲区定义架构来解决此问题。通过使用协议，DataStore 可以知道存储的类型，并且无需使用键便能提供类型。</li>
</ul>
<h5 data-id="heading-12">添加依赖项</h5>
<pre><code class="copyable">//1. 添加协议缓冲区插件
plugins &#123;
    ...
    id "com.google.protobuf" version "0.8.12"
&#125;

//2 添加协议缓冲区和 Proto DataStore 依赖项
implementation("androidx.datastore:datastore:1.0.0-rc02")
//protobuf
implementation  "com.google.protobuf:protobuf-javalite:3.10.0"
// optional - RxJava2 support
implementation("androidx.datastore:datastore-rxjava2:1.0.0-rc02")

//3. 配置协议缓冲区
protobuf &#123;
    // 设置 protoc 的版本
    protoc &#123;
        // //从仓库下载 protoc 这里的版本号需要与依赖 com.google.protobuf:protobuf-javalite:xxx 版本相同
        artifact = 'com.google.protobuf:protoc:3.10.0'
    &#125;
    generateProtoTasks &#123;
        all().each &#123; task ->
            task.builtins &#123;
                java &#123;
                    option "lite"
                &#125;
            &#125;
        &#125;
    &#125;

    // 默认生成目录 $buildDir/generated/source/proto 通过 generatedFilesBaseDir 改变生成位置
    generatedFilesBaseDir = "$projectDir/src/main"
&#125;

//4. 设置 proto 文件位置
android &#123;
    sourceSets &#123;
        main &#123;
            proto &#123;
                // proto 文件默认路径是 src/main/proto
                // 可以通过 srcDir 修改 proto 文件的位置
                srcDir 'src/main/proto'
            &#125;
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">定义架构</h5>
<ul>
<li>Proto DataStore 要求在 app/src/main/proto/ 目录的 proto 文件中保存预定义的架构。此架构用于定义在 Proto DataStore 中保存的对象的类型。如需详细了解如何定义 proto 架构，请参阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.cn%2Fprotocol-buffers%2Fdocs%2Fproto3" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.cn/protocol-buffers/docs/proto3" ref="nofollow noopener noreferrer">protobuf 语言指南</a>。</li>
<li>协议缓冲区是一种对结构化数据进行序列化的机制。只需对数据结构化的方式进行一次定义，编译器便会生成源代码，轻松写入和读取结构化数据。</li>
<li>在 app/src/main/proto 目录中创建一个名为 user_prefs.proto 的新文件,其内容如下</li>
</ul>
<pre><code class="copyable">syntax = "proto3"; //版本

//包名
option java_package = "com.jinyang.jetpackdemo.datastore";
option java_multiple_files = true;
option java_outer_classname = "UserInfoProto";

message User &#123;
    //格式：字段类型 + 字段名称 + 字段编号
    string name = 1
    int32 age = 2
    bool isMarried = 3;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建完成后，Rebuild Project，即可看到app/src/main/debug下自动生成的文件</li>
</ul>
<h5 data-id="heading-14">创建序列化器</h5>
<ul>
<li>自定义Serializer</li>
</ul>
<pre><code class="copyable">object UserSerializer:Serializer<User>&#123;
    override val defaultValue: User
        get() = User.getDefaultInstance()

    override suspend fun readFrom(input: InputStream): User &#123;
        return User.parseFrom(input)
    &#125;

    override suspend fun writeTo(t: User, output: OutputStream) &#123;
        t.writeTo(output)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">创建DataStore</h5>
<pre><code class="copyable">val Context.userInfoStore: DataStore<User> by dataStore(
    fileName = "userInfo.pb",
    serializer = UserSerializer
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">读写内容及在同步异步代码中的使用</h5>
<ul>
<li>请尽可能避免在 DataStore 数据读取时阻塞线程。阻塞界面线程可能会导致 ANR 或界面卡顿，而阻塞其他线程可能会导致死锁;</li>
</ul>
<pre><code class="copyable"> private fun dataStoreProto() &#123;
    // 注册观察者读取内容
    userInfoStore.data.asLiveData().observe(this) &#123;
        LjyLogUtil.d("asLiveData：it:$it")
        LjyLogUtil.d("name:$&#123;it.name&#125;")
        LjyLogUtil.d("age:$&#123;it.age&#125;")
        LjyLogUtil.d("isMarried:$&#123;it.isMarried&#125;")
    &#125;
    lifecycleScope.launch &#123;
        //将内容写入 Proto DataStore
        userInfoStore.updateData &#123;
            it.toBuilder()
                .setName("今阳")
                .setAge(18)
                .setIsMarried(true)
                .build()
        &#125;
        //使用collect读取内容
        userInfoStore.data.collect &#123;
            LjyLogUtil.d("collect: it:$it")
        &#125;
    &#125;
    // DataStore 的主要优势之一是异步 API，但可能不一定始终能将周围的代码更改为异步代码。
    // 如果您使用的现有代码库采用同步磁盘 I/O，或者您的依赖项不提供异步 API，就可能出现这种情况。
    // Kotlin 协程提供 runBlocking() 协程构建器，以帮助消除同步与异步代码之间的差异。
    // 您可以使用 runBlocking() 从 DataStore 同步读取数据。RxJava 在 Flowable 上提供阻塞方法。
    // 以下代码会阻塞发起调用的线程，直到 DataStore 返回数据：
    val user = runBlocking &#123; userInfoStore.data.first() &#125;
    LjyLogUtil.d("runBlocking: user:$user")
    //对界面线程执行同步 I/O 操作可能会导致 ANR 或界面卡顿。您可以通过从 DataStore 异步预加载数据来减少这些问题：
    lifecycleScope.launch &#123;
        val user = userInfoStore.data.first()
        LjyLogUtil.d("user:$user")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">迁移 SharedPreferences 到 Proto DataStore</h5>
<pre><code class="copyable">//1. 创建DataStore,并将sp的键值对映射到User
val Context.userInfoStore2: DataStore<User> by dataStore(
    fileName = "userInfo2.pb",
    serializer = UserSerializer,
    produceMigrations = &#123; context ->
        listOf(SharedPreferencesMigration(context, Constants.MY_SP) &#123; sharedPrefs, user ->
            //将sp的键值对映射到User
            user.toBuilder()
                .setName(sharedPrefs.getString(Constants.KEY_NAME_SP))
                .setAge(sharedPrefs.getInt(Constants.KEY_NAME_SP,0))
                .setIsMarried(false)
                .build()
        &#125;)
    &#125;
)
//2. 执行一次读写
lifecycleScope.launch &#123;
    val user = userInfoStore2.data.first()
    LjyLogUtil.d("user:$user")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">MMKV</h3>
<ul>
<li>替换sp还有另外一种比较不错的选择，就是腾讯开源的MMKV；</li>
<li>MMKV 是基于 mmap 内存映射的 key-value 组件，底层序列化/反序列化使用 protobuf 实现，性能高，稳定性强。从 2015 年中至今在微信上使用，其性能和稳定性经过了时间的验证。</li>
</ul>
<h4 data-id="heading-19">使用流程</h4>
<h5 data-id="heading-20">1. 添加依赖</h5>
<pre><code class="copyable">implementation 'com.tencent:mmkv-static:1.2.10'
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">2. 初始化，在Application.onCreate()中</h5>
<pre><code class="copyable">val rootDir = MMKV.initialize(this)
LjyLogUtil.d(rootDir)
//默认为：/data/user/0/com.jinyang.jetpackdemo/files/mmkv
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">3. CRUD</h5>
<pre><code class="copyable">//获取单例
val kv = MMKV.defaultMMKV()
//写入数据
kv.encode("name", "LJY")
kv.encode("age", 16)
kv.encode("isMarried", true)
//读取数据
val name = kv.decodeString("name")
LjyLogUtil.d("name=$name")
val age = kv.decodeInt("age")
LjyLogUtil.d("age=$age")
val isMarried = kv.decodeBool("isMarried")
LjyLogUtil.d("isMarried=$isMarried")
//删除数据
kv.removeValueForKey("age");
LjyLogUtil.d("age=$&#123;kv.decodeInt("age")&#125;")
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">4. 如果不同业务需要区别存储，也可以单独创建自己的实例</h5>
<pre><code class="copyable">val kvUser = MMKV.mmkvWithID("userInfo")
kvUser.encode("name", "yang")
LjyLogUtil.d("name=$&#123;kvUser.decodeString("name")&#125;")
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">5. 如果业务需要多进程访问，那么在初始化的时候加上标志位 MMKV.MULTI_PROCESS_MODE</h5>
<pre><code class="copyable">val kvSetting = MMKV.mmkvWithID("settings", MMKV.MULTI_PROCESS_MODE)
kvSetting.encode("key", "abc")
LjyLogUtil.d("key=$&#123;kvSetting.decodeString("key")&#125;")
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">6. 迁移 SharedPreferences 到 MMKV</h5>
<ul>
<li>MMKV 还额外实现了一遍 SharedPreferences、SharedPreferences.Editor 这两个 interface，
在迁移的时候只需两三行代码即可，其他 CRUD 操作代码都不用改</li>
</ul>
<pre><code class="copyable">// val preferences = getSharedPreferences("myData", MODE_PRIVATE)
val sp2mmkv: MMKV = MMKV.mmkvWithID("myData")
// 迁移旧数据:
val sp = getSharedPreferences(Constants.MY_SP, MODE_PRIVATE)
sp2mmkv.importFromSharedPreferences(sp)
sp.edit().clear().apply()
// 跟以前用法一样
sp2mmkv.edit(commit = true)&#123;
    putBoolean("bool", true)
    val set = HashSet<String>()
    set.add("a")
    set.add("b")
    set.add("c")
    putStringSet("string-set", set)
&#125;
LjyLogUtil.d("name=$&#123;sp2mmkv.getString(Constants.KEY_NAME_SP,"")&#125;")
LjyLogUtil.d("age=$&#123;sp2mmkv.getInt(Constants.KEY_AGE_SP,0)&#125;")
LjyLogUtil.d("bool=$&#123;sp2mmkv.getBoolean("bool",false)&#125;")
LjyLogUtil.d("string-set=$&#123;sp2mmkv.getStringSet("string-set", emptySet())&#125;")
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">我是今阳，如果想要进阶和了解更多的干货，欢迎关注微信公众号 “今阳说” 接收我的最新文章</h3></div>  
</div>
            