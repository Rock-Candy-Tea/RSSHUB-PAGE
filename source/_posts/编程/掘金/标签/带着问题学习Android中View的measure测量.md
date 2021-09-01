
---
title: '带着问题学习Android中View的measure测量'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f93d91bd7e124f75a1c5510bb3b7c066~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 16:13:53 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f93d91bd7e124f75a1c5510bb3b7c066~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<p>在进行研究measure原理之前，我们先带着这三个问题来想想。因为我是遇到这三个问题才开始研究measure的源码，所以我也把下面的三个问题当做引子。</p>
<p>调用measure(int widthMeasureSpec, int heightMeasureSpec)方法传递的参数是什么？
为什么调用measure方法View控件没有进行测量？
如何强制view进行测量？
在进行研究之前，我们先来看一个简单的布局，</p>
<pre><code class="hljs language-xml copyable" lang="xml">        <span class="hljs-tag"><<span class="hljs-name">Button</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/btn_click"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:text</span>=<span class="hljs-string">"点击"</span>
            <span class="hljs-attr">android:onClick</span>=<span class="hljs-string">"start"</span>
            /></span>
        <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/linear"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:background</span>=<span class="hljs-string">"#FF0000"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Button</span>
                <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"wrap_content"</span>
                <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
                <span class="hljs-attr">android:text</span>=<span class="hljs-string">"点击"</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f93d91bd7e124f75a1c5510bb3b7c066~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据布局文件，我们并没有设置边距属性，为什么显示的效果的Button跟下面的没有对齐。这就是。在实际开发中，我们细心点会发现，对于Button控件，我们选中它的时候显示的区域比它展现的区域大。</p>
<p>如果我们给Button控件添加背景色：</p>
<pre><code class="hljs language-xml copyable" lang="xml">        <span class="hljs-tag"><<span class="hljs-name">Button</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/btn_click"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:text</span>=<span class="hljs-string">"点击"</span>
            <span class="hljs-attr">android:background</span>=<span class="hljs-string">"#FF0000"</span>
            <span class="hljs-attr">android:onClick</span>=<span class="hljs-string">"start"</span>
            /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到Button的背景色和LinearLayout的背景色无缝连接在一起，同时我们观察下面的那个点击的Button，发现它的周围区域实际是存在的，是白色与我们的背景色重叠起来了。这就引入了我们的一个重要概念:控件边界布局和视觉编辑布局。我们在真机上打开【显示布局边界】，在设置——>开发者选项——>显示布局边界。
我们看下效果图。</p>
<p>注：蓝色 为控件的布局边界；粉红色为视觉边界
这就涉及到我们的一个ViewGroup属性：android:layoutMode</p>
<p>说的通俗一点，clipBounds就是默认值，不处理一些控件之间的“留白”，opticalBounds消除控件之间的留白。</p>
<p>我们抽出LinearLayout的布局来说：</p>
<pre><code class="hljs language-xml copyable" lang="xml">        <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/linear"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:background</span>=<span class="hljs-string">"#fff000"</span>
            <span class="hljs-attr">android:layoutMode</span>=<span class="hljs-string">"clipBounds"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Button</span>
                <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"wrap_content"</span>
                <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
                <span class="hljs-attr">android:text</span>=<span class="hljs-string">"点击"</span>/></span>
            <span class="hljs-tag"><<span class="hljs-name">TextView</span> 
                <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"wrap_content"</span>
                <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
                <span class="hljs-attr">android:text</span>=<span class="hljs-string">"测试的"</span>
                /></span>
        <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们修改属性android:layoutMode=”opticalBounds”，效果图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e3e188c4b35464f8c0ab14dad6183e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过对比发现就是一个清除的效果。</p>
<p>MeasureSpec
我们分析第一个问题，onMeasure()方法里传的是什么？传的就是MeasureSpec变量。它是View的一个内部类。源码设计非常简单精悍。</p>
<p>一个MeasureSpec封装了父布局传递给子布局的布局要求，每个MeasureSpec代表了一组宽度和高度的要求。一个MeasureSpec由大小和模式组成。由32位组成，头8位为模式，后24位封装大小。它有三种模式：UNSPECIFIED(未指定),父元素部队自元素施加任何束缚，子元素可以得到任意想要的大小；EXACTLY(完全)，父元素决定自元素的确切大小，子元素将被限定在给定的边界里而忽略它本身大小；AT_MOST(至多)，子元素至多达到指定大小的值。它常用的三个函数：</p>
<p>static int getMode(int measureSpec):根据提供的测量值(格式)提取模式(上述三个模式之一)
static int getSize(int measureSpec):根据提供的测量值(格式)提取大小值(这个大小也就是我们通常所说的大小)
static int makeMeasureSpec(int size,int mode):根据提供的大小值和模式创建一个测量值(格式)
Mode的取值：</p>
<p>MeasureSpec.AT_MOST，即十进制2，该值表示View最大可以取其父ViewGroup给其指定的尺寸，例如现在有个Int值widthMeasureSpec，ViewGroup将其传递给了View的measure方法，如果widthMeasureSpec中的mode值是AT_MOST，size是300，那么表示View能取的最大的宽度是300。</p>
<p>MeasureSpec.EXACTLY，即十进制1，该值表示View必须使用其父ViewGroup指定的尺寸，还是以widthMeasureSpec为例，如果其mode值是EXACTLY，控件大小就是它老子的大小</p>
<p>MeasureSpec.UNSPECIFIED，即十进制0，该值表示View的父ViewGroup没有给View在尺寸上设置限制条件，这种情况下View可以忽略measureSpec中的size，View可以取自己想要的值作为量算的尺寸。</p>
<p>我们常看到measure(0,0)或者measure(1,1)之类的，这就是传入的测量模式。</p>
<p>measure()方法
下面就开始分析measure方法。</p>
<pre><code class="hljs language-java copyable" lang="java">       <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">void</span> <span class="hljs-title">measure</span><span class="hljs-params">(<span class="hljs-keyword">int</span> widthMeasureSpec, <span class="hljs-keyword">int</span> heightMeasureSpec)</span> </span>&#123;
            <span class="hljs-comment">//判断当前view的LayoutMode是否为opticalbounds</span>
            <span class="hljs-keyword">boolean</span> optical = isLayoutModeOptical(<span class="hljs-keyword">this</span>);
            <span class="hljs-keyword">if</span> (optical != isLayoutModeOptical(mParent)) &#123;<span class="hljs-comment">//判断当前view的ParentView的LayoutMode是否为opticalbounds</span>
                Insets insets = getOpticalInsets();
                <span class="hljs-keyword">int</span> oWidth  = insets.left + insets.right;
                <span class="hljs-keyword">int</span> oHeight = insets.top  + insets.bottom;
                widthMeasureSpec  = MeasureSpec.adjust(widthMeasureSpec,  optical ? -oWidth  : oWidth);
                heightMeasureSpec = MeasureSpec.adjust(heightMeasureSpec, optical ? -oHeight : oHeight);
            &#125;

            <span class="hljs-comment">// 根据我们传入的widthMeasureSpec和heightMeasureSpec计算key值，我们在mMeasureCache中存储我们view的信息</span>
            <span class="hljs-keyword">long</span> key = (<span class="hljs-keyword">long</span>) widthMeasureSpec << <span class="hljs-number">32</span> | (<span class="hljs-keyword">long</span>) heightMeasureSpec & <span class="hljs-number">0xffffffffL</span>;
            <span class="hljs-comment">//如果mMeasureCache为null，则进行new一个对象</span>
            <span class="hljs-keyword">if</span> (mMeasureCache == <span class="hljs-keyword">null</span>) mMeasureCache = <span class="hljs-keyword">new</span> LongSparseLongArray(<span class="hljs-number">2</span>);

            <span class="hljs-comment">//mOldWidthMeasureSpec和mOldHeightMeasureSpec分别表示上次对View进行量算时的widthMeasureSpec和heightMeasureSpec</span>
            <span class="hljs-comment">//执行View的measure方法时，View总是先检查一下是不是真的有必要费很大力气去做真正的量算工作</span>
            <span class="hljs-comment">//mPrivateFlags是一个Int类型的值，其记录了View的各种状态位</span>
            <span class="hljs-comment">//如果(mPrivateFlags & PFLAG_FORCE_LAYOUT) == PFLAG_FORCE_LAYOUT，</span>
            <span class="hljs-comment">//那么表示当前View需要强制进行layout（比如执行了View的forceLayout方法），所以这种情况下要尝试进行量算</span>
            <span class="hljs-comment">//如果新传入的widthMeasureSpec/heightMeasureSpec与上次量算时的mOldWidthMeasureSpec/mOldHeightMeasureSpec不等，</span>
            <span class="hljs-comment">//那么也就是说该View的父ViewGroup对该View的尺寸的限制情况有变化，这种情况下要尝试进行量算</span>
            <span class="hljs-keyword">if</span> ((mPrivateFlags & PFLAG_FORCE_LAYOUT) == PFLAG_FORCE_LAYOUT ||
                    widthMeasureSpec != mOldWidthMeasureSpec ||
                    heightMeasureSpec != mOldHeightMeasureSpec) &#123;

                <span class="hljs-comment">//通过运算，重置mPrivateFlags值，即View的测量状态</span>
                mPrivateFlags &= ~PFLAG_MEASURED_DIMENSION_SET;
                <span class="hljs-comment">//解决布局中的Rtl问题</span>
                resolveRtlPropertiesIfNeeded();
                <span class="hljs-comment">//判断当前View是否是强制进行测量，如果是则将cacheIndex=-1，反之从mMeasureCache中获取</span>
                <span class="hljs-comment">//对应的index，即从缓存中读取存储的大小。</span>
                <span class="hljs-keyword">int</span> cacheIndex = (mPrivateFlags & PFLAG_FORCE_LAYOUT) == PFLAG_FORCE_LAYOUT ? -<span class="hljs-number">1</span> :
                        mMeasureCache.indexOfKey(key);
                <span class="hljs-comment">//根据cacheIndex的大小判断是否需要重新测量，或者根据布尔变量sIgnoreMeasureCache进行判断。</span>
                <span class="hljs-keyword">if</span> (cacheIndex < <span class="hljs-number">0</span> || sIgnoreMeasureCache) &#123;
                    <span class="hljs-comment">// 重新测量，则调用我们重写的onMeasure()方法进行测量，然后重置View的状态</span>
                    onMeasure(widthMeasureSpec, heightMeasureSpec);
                    mPrivateFlags3 &= ~PFLAG3_MEASURE_NEEDED_BEFORE_LAYOUT;
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-comment">//  通过我们计算的cacheIndex值，从缓存中读取我们的测量值。</span>
                    <span class="hljs-keyword">long</span> value = mMeasureCache.valueAt(cacheIndex);
                    <span class="hljs-comment">// 通过setMeasuredDimension()方法设置我们的测量值，然后重置View的状态</span>
                    setMeasuredDimension((<span class="hljs-keyword">int</span>) (value >> <span class="hljs-number">32</span>), (<span class="hljs-keyword">int</span>) value);
                    mPrivateFlags3 |= PFLAG3_MEASURE_NEEDED_BEFORE_LAYOUT;
                &#125;

                <span class="hljs-comment">// 如果View的状态没有改变，则会抛出异常“我们没有调用”setMeasuredDimension()“方法，一般出现在我们重写onMeasure方法，</span>
                <span class="hljs-comment">//但是没有调用setMeasuredDimension方法导致的。</span>
                <span class="hljs-keyword">if</span> ((mPrivateFlags & PFLAG_MEASURED_DIMENSION_SET) != PFLAG_MEASURED_DIMENSION_SET) &#123;
                    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalStateException(<span class="hljs-string">"onMeasure() did not set the"</span>
                            + <span class="hljs-string">" measured dimension by calling"</span>
                            + <span class="hljs-string">" setMeasuredDimension()"</span>);
                &#125;

                mPrivateFlags |= PFLAG_LAYOUT_REQUIRED;
            &#125;

            mOldWidthMeasureSpec = widthMeasureSpec;
            mOldHeightMeasureSpec = heightMeasureSpec;
            <span class="hljs-comment">//将最新的widthMeasureSpec和heightMeasureSpec进行存储到mMeasureCache</span>
            mMeasureCache.put(key, ((<span class="hljs-keyword">long</span>) mMeasuredWidth) << <span class="hljs-number">32</span> |
                    (<span class="hljs-keyword">long</span>) mMeasuredHeight & <span class="hljs-number">0xffffffffL</span>); <span class="hljs-comment">// suppress sign extension</span>
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，注释还算详细，仔细看应该能知道测量的流程。
（1）、测量首先判断控件的模式，通过调用isLayoutModeOptical方法进行判断。</p>
<pre><code class="hljs language-java copyable" lang="java">        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isLayoutModeOptical</span><span class="hljs-params">(Object o)</span> </span>&#123;
            <span class="hljs-keyword">return</span> o <span class="hljs-keyword">instanceof</span> ViewGroup && ((ViewGroup) o).isLayoutModeOptical();
        &#125;

        <span class="hljs-comment">//ViewGroup的isLayoutModeOptical方法</span>
        <span class="hljs-function"><span class="hljs-keyword">boolean</span> <span class="hljs-title">isLayoutModeOptical</span><span class="hljs-params">()</span> </span>&#123;
            <span class="hljs-keyword">return</span> mLayoutMode == LAYOUT_MODE_OPTICAL_BOUNDS;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法就是判断view是否为ViewGroup类型，然后判断layoutMode设定是否为opticalBounds。如果是，则对传入的widthMeasureSpec、heightMeasureSpec进行重新计算封装，通过上面的试验，我们看到了设定的区别，所以需要重新计算封装。</p>
<p>（2）、判断当前view是否强制重新计算，或者传入进来的MeasureSpec是否和上次不同。这两种情况满足一种则进行测量运算。
（3）、系统还不满足，又判断是否为强制测量，如果为强制测量或者忽略缓存，则调用我们重写的onMeasure()方法进行测量，反之，从mMeasureCache缓存中读取上次的测量数据。</p>
<p>为什么调用measure()方法控件没有进行重新测量？</p>
<p>通过前面的源码分析，是不是对结果知道一二，View也不是因为我们调用了measure方法就进行真真切切的重新测量，首先，它会判断我们是否是强制测量或者测量模式发生了改变没有，这个是必要条件，如果这里都不满足就不会进入执行到我们的onMeasure方法，之后还要判断我们是否强制重新测量，不然取缓存的值，只样实际上还没有达到我们的测量。
注：Android不同版本对应的measure方法源码可能有所不同。</p>
<p>说到这里，measure的源码是分析了，我们在往深入的想，我们如果在我们的自定义View时没有对onMeasure()方法进行重写，那么系统调用的onMeasure()方法是怎么实现的呢？不错，我们就瞧一瞧View中默认的onMeasure()方法是怎么实现的。</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onMeasure</span><span class="hljs-params">(<span class="hljs-keyword">int</span> widthMeasureSpec, <span class="hljs-keyword">int</span> heightMeasureSpec)</span> </span>&#123;
        setMeasuredDimension(getDefaultSize(getSuggestedMinimumWidth(), widthMeasureSpec),
                getDefaultSize(getSuggestedMinimumHeight(), heightMeasureSpec));
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里面涉及到三个方法：</p>
<ul>
<li>getDefaultSize</li>
<li>getSuggestedMinimumWidth</li>
<li>getSuggestedMinimumHeight</li>
</ul>
<p>稍微思考下，我们也知道肯定是设置一个默认值的，我们看下后两个函数的源码：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getSuggestedMinimumWidth</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> (mBackground == <span class="hljs-keyword">null</span>) ? mMinWidth : max(mMinWidth, mBackground.getMinimumWidth());
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getSuggestedMinimumHeight</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> (mBackground == <span class="hljs-keyword">null</span>) ? mMinHeight : max(mMinHeight, mBackground.getMinimumHeight());
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>都是进行判断backgroud是否为空，如果为空，返回view最小的高度或宽度，如果不为空，返回与backgroud的最小宽高中的最大值。可能你会疑惑，view的最小宽度或高度是怎么来的？这个就要回归到我们的View构造函数。</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-keyword">case</span> R.styleable.View_minWidth:
        mMinWidth = a.getDimensionPixelSize(attr, <span class="hljs-number">0</span>);
        <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> R.styleable.View_minHeight:
        mMinHeight = a.getDimensionPixelSize(attr, <span class="hljs-number">0</span>);
        <span class="hljs-keyword">break</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以从这里获取，当然我们也可以进行设定：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMinimumWidth</span><span class="hljs-params">(<span class="hljs-keyword">int</span> minWidth)</span> </span>&#123;
        mMinWidth = minWidth;
        requestLayout();
    &#125;


    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMinimumHeight</span><span class="hljs-params">(<span class="hljs-keyword">int</span> minHeight)</span> </span>&#123;
        mMinHeight = minHeight;
        requestLayout();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们接着看看看getDefaultSize()的源码：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getDefaultSize</span><span class="hljs-params">(<span class="hljs-keyword">int</span> size, <span class="hljs-keyword">int</span> measureSpec)</span> </span>&#123;
        <span class="hljs-keyword">int</span> result = size;
        <span class="hljs-keyword">int</span> specMode = MeasureSpec.getMode(measureSpec);
        <span class="hljs-keyword">int</span> specSize = MeasureSpec.getSize(measureSpec);

        <span class="hljs-keyword">switch</span> (specMode) &#123;
        <span class="hljs-keyword">case</span> MeasureSpec.UNSPECIFIED:
            result = size;
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> MeasureSpec.AT_MOST:
        <span class="hljs-keyword">case</span> MeasureSpec.EXACTLY:
            result = specSize;
            <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">return</span> result;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在getDefaultSize中，传入进来我们获取的最小值，然后根据我们设定的MeasureSpec获取对应size和mode，然后判断mode，如果为MeasureSpec.UNSPECIFIED就将size赋值我们获取的最小大小。模式为MeasureSpec.AT_MOST、MeasureSpec.EXACTLY时，赋值为我们从MeasureSpec获取的大小。这也证实了自定义控件时，我们没有重写onMeasure方法，同时给控件设置wrap_content属性，控件显示的效果是match_parent的效果。</p>
<p>说到这里measure流程的大概也基本搞明白了。
我们来看第三个问题，如何强制一个view进行重绘？
根据上面的分析，我们强制重绘就得清除缓存mMeasureCache缓存中的数据。这里就得提及forceLayout()方法，看下这个方法的源码：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">forceLayout</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (mMeasureCache != <span class="hljs-keyword">null</span>) mMeasureCache.clear();
        mPrivateFlags |= PFLAG_FORCE_LAYOUT;
        mPrivateFlags |= PFLAG_INVALIDATED;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法中就是清除缓存mMeasureCache中的缓存数据，然后改变View的mPrivateFlags属性值。这里又得说起requestLayout()函数，用于请求重新布局。</p>
<pre><code class="hljs language-java copyable" lang="java">
       <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">requestLayout</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (mMeasureCache != <span class="hljs-keyword">null</span>) mMeasureCache.clear();

        <span class="hljs-keyword">if</span> (mAttachInfo != <span class="hljs-keyword">null</span> && mAttachInfo.mViewRequestingLayout == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-comment">// Only trigger request-during-layout logic if this is the view requesting it,</span>
            <span class="hljs-comment">// not the views in its parent hierarchy</span>
            ViewRootImpl viewRoot = getViewRootImpl();
            <span class="hljs-keyword">if</span> (viewRoot != <span class="hljs-keyword">null</span> && viewRoot.isInLayout()) &#123;
                <span class="hljs-keyword">if</span> (!viewRoot.requestLayoutDuringLayout(<span class="hljs-keyword">this</span>)) &#123;
                    <span class="hljs-keyword">return</span>;
                &#125;
            &#125;
            mAttachInfo.mViewRequestingLayout = <span class="hljs-keyword">this</span>;
        &#125;

        mPrivateFlags |= PFLAG_FORCE_LAYOUT;
        mPrivateFlags |= PFLAG_INVALIDATED;

        <span class="hljs-keyword">if</span> (mParent != <span class="hljs-keyword">null</span> && !mParent.isLayoutRequested()) &#123;
            mParent.requestLayout();
        &#125;
        <span class="hljs-keyword">if</span> (mAttachInfo != <span class="hljs-keyword">null</span> && mAttachInfo.mViewRequestingLayout == <span class="hljs-keyword">this</span>) &#123;
            mAttachInfo.mViewRequestingLayout = <span class="hljs-keyword">null</span>;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以完成View的强制测量。在实际的开发中，我们在对自定义View进行测量的时候，只需要重写onMeasure()方法即可，在onMeasure()方法中指定我们要求的控件大小，除非我们在刷新控件的时候需要我们去考虑一些方法的实现，探究源码让我们知道了为什么是这样，不至于迷惘。</p></div>  
</div>
            