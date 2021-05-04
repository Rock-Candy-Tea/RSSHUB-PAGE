
---
title: 'UI组件化--干掉shape终极一战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef7d9aa9ce9a44e4b6cc8e40cabf8156~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 17:42:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef7d9aa9ce9a44e4b6cc8e40cabf8156~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>UI组件化对项目有正向收益，不仅能提效，还能保证高度的视觉还原度，减少和UI设计师沟通成本，所以也得到了大家的认可。所以每个项目都会启动UI组件化建设，但是UI视图是和项目强相关的，项目间无法复用，导致大家疲于实现，重复造轮子，拖延下班时间，那么基于上面的背景，有没有更好的解决方案呢，答案是有的，下面介绍一下UI组件化在项目中的实施经验，下面分为<strong>目标</strong>、<strong>工程架构</strong>、<strong>组件架构</strong>、<strong>组件实现</strong>来展开。</p>
<h2 data-id="heading-1">目标</h2>
<p>对现有UI组件化进行<strong>容器化</strong>抽象，底层UI组件提供最大功能集合，完全解耦业务逻辑，业务方根据自己需求，基于基础组件开发，通过属性配置或者组合的方式达到复杂的效果，所以只要底层组件抽象的足够好、能力足够全，就能大大的提高开发效率，后期适配也不会涉及核心逻辑修改，一定程度的保证了功能的稳定性</p>
<h2 data-id="heading-2">工程架构</h2>
<h4 data-id="heading-3">module划分</h4>
<p>所有的ui组件统一收敛到uikit下，其下面moudle划分以是否非常通用为依据，如果非业务属性，并且特别通用的模块组件，抽取单独module，方便解耦和复用，如果不是则统一放在同一个module下，这样uikit模块划分如下：</p>
<ul>
<li><strong>app</strong></li>
</ul>
<p>空壳工程，可以单独运行</p>
<ul>
<li><strong>demo</strong></li>
</ul>
<p>对所有的组件提供demo，里面的功能也可以在调试面板中打开</p>
<ul>
<li><strong>uikit</strong></li>
</ul>
<p>依赖<strong>widget<strong><strong>和</strong></strong>module****，业务使用ui组件直接依赖<strong><strong>uikit</strong></strong>即可</strong></p>
<ul>
<li>
<p><strong>widget</strong></p>
<ul>
<li>DivideLine</li>
</ul>
</li>
<li>
<p>XRadioGroup</p>
</li>
<li>
<p>LoadingView</p>
</li>
<li>
<p>ShimmerLayout</p>
</li>
<li>
<p>...</p>
</li>
<li>
<p><strong>uikit-module</strong></p>
<ul>
<li><strong>flatButton</strong></li>
</ul>
</li>
<li>
<p><strong>roundView</strong></p>
</li>
<li>
<p><strong>load</strong></p>
</li>
<li>
<p><strong>dialog</strong></p>
</li>
<li>
<p><strong>imageSelect</strong></p>
</li>
<li>
<p><strong>toast</strong></p>
</li>
<li>
<p>...</p>
</li>
</ul>
<h4 data-id="heading-4">工程分层</h4>
<p>工程架构可以分为5层，分别是：基础控件、组合控件、业务UI组件、桥接、demo。</p>
<ul>
<li>
<p>基础控件：提供原子能力，单点控件，比如层叠布局FlowLayout、骨架控件ShimmerLayout、按钮Flatbutton</p>
</li>
<li>
<p>组合控件：会依赖基础控件，比如Dialog、ImageSelector，这些控件UI会比较复杂，所以会用到FlatButton、ShimmerLayout等基础组件来提高开发效率</p>
</li>
<li>
<p>业务UI组件：这个就是我们真正要实现的UI组件，基于设计要求定制开发，在基础控件和组合控件上配置业务偏好，组合成业务组件，开发工作量比较小</p>
</li>
<li>
<p>桥接：业务层不感知UI组件的个数和依赖关系，业务层只依赖uikit，而UI组件的依赖管理收敛到uikit中，这样的好处就是，后续迭代只在uikit维护依赖关系即可</p>
</li>
<li>
<p>Demo: 一个好的组件除了使用文档，还需要有直观的示例代码，demo可以直接集成到调试面板中</p>
</li>
</ul>
<p>架构分层如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef7d9aa9ce9a44e4b6cc8e40cabf8156~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个好的架构应该层次分明、低耦合、高扩展，对组件的增删支持的足够友好，任何组件都能准确的找到对应的分层，并且不会改动到已有代码，所以review一下刚刚设计的架构，基本上满足需求，架构设计符合预期。架构设计好之后的步骤就是实施了，如何和现有的工程做结合呢，UI组件按阶段可以分为：开发阶段、稳定阶段，理想的开发模式为开发阶段在宿主工程中开发调试，但是放宿主工程中会带了编译慢的问题，组件开发和业务是接耦的，所以希望代码在宿主工程，demo和组件开发可以单独运行，当组件开发完成，到了稳定阶段，组件代码修改频率降低，同时加快编译速度，UIKit组件发布到远程maven仓库，最终uikit工程独立出来，单独迭代，下面是工程架构实现</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22c3664b875a4181beed64b997d8dbcd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>UI组件和宿主打包编译</p>
<p>settings.gradle</p>
<pre><code class="copyable">includeIfAbsent ':uikit:uikit'
includeIfAbsent ':uikit:demo'
includeIfAbsent ':uikit:imgselector'
includeIfAbsent ':uikit:roundview'
includeIfAbsent ':uikit:widget'
includeIfAbsent ':uikit:photodraweeview'
includeIfAbsent ':uikit:flatbutton'
includeIfAbsent ':uikit:dialog'
includeIfAbsent ':uikit:widgetlayout'
includeIfAbsent ':uikit:statusbar'
includeIfAbsent ':uikit:toolbar'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>common_business.gradle中一键依赖</p>
<pre><code class="copyable">apply from: rootProject.file("library_base.gradle")

dependencies &#123;
    .​..
    implementation project(":uikit:uikit")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UI组件独立编译</p>
<p>uikit/shell/settings.gradle</p>
<pre><code class="copyable">include ':app'
includeModule('widget','../')
includeModule('demo','../')
includeModule('flatbutton','../')
includeModule('imgselector','../')
includeModule('photodraweeview','../')
includeModule('roundview','../')
includeModule('uikit','../')
includeModule('widgetlayout','../')
includeModule('dialog','../')
includeModule('statusbar','../')
includeModule('toolbar','../')

def includeModule(name, filePath = name) &#123;
    def projectDir = new File(filePath+name)
    if (projectDir.exists()) &#123;
        include ':uikit:' + name
        project(':uikit:' + name).projectDir = projectDir
    &#125; else &#123;
        print("settings:could not find module $name in path $filePath")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UI组件lib的build.gradle中</p>
<pre><code class="copyable">if (rootProject.ext.is_in_uikit_project) &#123;
    apply from: rootProject.file('../uikit.gradle')
&#125; else &#123;
    apply from: rootProject.file('uikit/uikit.gradle')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就实现了宿主工程UIKit代码单独运行的效果了</p>
<h2 data-id="heading-5">组件架构</h2>
<p>组件可以分为2类：工具型、业务类型，2个类型的组件迭代思路差异非常的大，工具型组件，只要单点做到极致就ok了，整体比较简单，复用性也比较强，而业务型组件就会稍显复杂，既要考虑复用性，也要考虑可扩展性，下面分别介绍这2个类型组件的实现思路</p>
<h4 data-id="heading-6">工具型</h4>
<p>工具型组件迭代的思路就是不断的完善基础能力，尽可能的功能全面，在已有的能力上不断的支持新的功能，比较重要的就是兼容已有api，比较代表性的组件有FlatButton、RoundView、StatusBar，可以参考下FlatButton&RoundView迭代历程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3548199c00be451da886045fe9b2e597~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">业务型</h4>
<p>如何做好一个业务组件呢，实现可以是具象的，也可以是抽象的，好的组件设计应该是2者兼备，最底层的实现应该是足够抽象，而上层实现又应该是具象的，所以需要带着容器化的思路来实现，那么怎么个思路呢，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91b36b4acb624b88beb9082986f6d00f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">组件实现</h2>
<p>下面以FlatButton为例介绍组件实现方式，其它组件实现思路类似。在实现前，我们先看下视觉稿</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27e63ef993764c5093662a729aa10fac~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按钮样式特别多，实现方式也可以有很多种，现有工程也给出了实现方案，具体如下：</p>
<p>第一步：分别定义noraml下的shape和pressed的shape，如果enable = false，还得再定义一个dissable的shape</p>
<p><strong>normal (ui_standard_bg_btn_corner_28_ripple)</strong></p>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android"
    android:color="@color/button_pressed_cover">
    <item
        android:drawable="@drawable/ui_standard_bg_btn_corner_28_enable">
    </item>

</ripple>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>pressed(ui_standard_bg_btn_corner_28_disable)</strong></p>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <gradient
        android:angle="0"
        android:endColor="@color/button_disable_end"
        android:startColor="@color/button_disable_start"
        android:useLevel="false"
        android:type="linear" />
    <corners android:radius="28dp" />
</shape>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步：定义selector</p>
<p><strong>selector(ui_standard_bg_btn_corner_28)</strong></p>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_enabled="true" android:drawable="@drawable/ui_standard_bg_btn_corner_28_ripple" />
    <item android:state_enabled="false" android:drawable="@drawable/ui_standard_bg_btn_corner_28_disable" />
</selector>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步：使用</p>
<pre><code class="copyable"><TextView
    ...
    android:background="@drawable/ui_standard_bg_btn_corner_28"
    android:textColor="@color/white"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样按钮的背景按压就实现了，如果在此基础上，文字也需要按压态，那么就重复上面的步骤，对颜色再创建一个选择器，当实现完上面UI定义的样式后，工程中的画风如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c75281fd4ce4e7db046089fd76ea491~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>我是谁，我在哪里，这该怎么玩</strong>，长得都差不多，基本没有开发体验，复用性、扩展性都非常的差，如果来个UI大改版，又得从头再来一次。那怎么解决上面的问题呢，答案是定义按钮通用能力，业务上层再实现，按这个思路做，需要删除上面所有shape、selector，然后自定义控件，我们都知道，上面定义的shape、selector xml文件，android系统最终都是会解析生成对应的对象，所以我们借鉴一下系统代码，实现起来就so easy</p>
<p>看下这个shape xml</p>
<pre><code class="copyable"><shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <gradient
        android:angle="0"
        android:endColor="@color/button_disable_end"
        android:startColor="@color/button_disable_start"
        android:useLevel="false"
        android:type="linear" />
    <corners android:radius="28dp" />
</shape>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析后的对象为GradientDrawable</p>
<pre><code class="copyable">public void setOrientation(Orientation orientation)
public void setColors(@Nullable @ColorInt int[] colors)
public void setCornerRadii(@Nullable float[] radii)
public void setStroke(int width, @ColorInt int color)
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，xml中定义的属性，代码中都可以实现，除了GradientDrawable，还会用到RippleDrawable实现水波纹，同理文字颜色选择器代码中对应的为ColorStateList，有了上面铺垫，具体实现如下：</p>
<h5 data-id="heading-9">第一步：定义自定义属性</h5>
<pre><code class="copyable"><declare-styleable name="FlatButton">
    <!--默认背景颜色 -->
    <attr name="fb_colorNormal" format="color" />
    <!--按下背景颜色 -->
    <attr name="fb_colorPressed" format="color" />
    <!--Disable背景颜色 -->
    <attr name="fb_colorDisable" format="color" />
    <!--默认开始渐变颜色 -->
    <attr name="fb_colorNormalStart" format="color" />
    <!--默认结束渐变颜色 -->
    <attr name="fb_colorNormalEnd" format="color" />
    <!--按下开始渐变颜色 -->
    <attr name="fb_colorPressedStart" format="color" />
    <!--按下结束渐变颜色 -->
    <attr name="fb_colorPressedEnd" format="color" />
    <!--Disable开始渐变颜色 -->
    <attr name="fb_colorDisableStart" format="color" />
    <!--Disable结束渐变颜色 -->
    <attr name="fb_colorDisableEnd" format="color" />
    <!--渐变方向 -->
    <attr name="fb_gradientOrientation">
        <enum name="left_right" value="0" />
        <enum name="right_left" value="1" />
        <enum name="top_bottom" value="2" />
        <enum name="bottom_top" value="3" />
        <enum name="tr_bl" value="4" />
        <enum name="bl_tr" value="5" />
        <enum name="br_tl" value="6" />
        <enum name="tl_br" value="7" />
    </attr>

    <!--默认文字颜色 -->
    <attr name="fb_colorNormalText" format="color" />
    <!--按下文字颜色 -->
    <attr name="fb_colorPressedText" format="color" />
    <!--Disable文字颜色 -->
    <attr name="fb_colorDisableText" format="color" />

    <!--边框颜色 -->
    <attr name="fb_strokeColor" format="color" />
    <!--按下边框颜色 -->
    <attr name="fb_strokePressColor" format="color" />
    <!--Disable边框颜色 -->
    <attr name="fb_strokeDisableColor" format="color" />
    <!--边框宽度 -->
    <attr name="fb_strokeWidth" format="dimension" />

    <!--水波纹是否可用 -->
    <attr name="fb_isRippleEnable" format="boolean" />
    <!--默认水波纹颜色 -->
    <attr name="fb_colorRippleNormal" format="color" />
    <!--按下水波纹颜色 -->
    <attr name="fb_colorRipplePressed" format="color" />

    <!--圆角角度 -->
    <attr name="fb_cornerRadius" format="dimension" />
    <!--左上圆角角度 -->
    <attr name="fb_radius_TL" format="dimension" />
    <!--右上圆角角度 -->
    <attr name="fb_radius_TR" format="dimension" />
    <!--左下圆角角度 -->
    <attr name="fb_radius_BL" format="dimension" />
    <!--右下圆角角度 -->
    <attr name="fb_radius_BR" format="dimension" />

    <!--是否开启防抖 -->
    <attr name="fb_antiShakeEnable" format="boolean" />
</declare-styleable>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">第二步：核心实现逻辑</h5>
<pre><code class="copyable">private fun setBackgroundCompat() &#123;
    val stateListDrawable = createStateListDrawable()
    val pL = paddingLeft
    val pT = paddingTop
    val pR = paddingRight
    val pB = paddingBottom
    background = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP && isRippleEnable) &#123;
        val rippleDrawable = RippleDrawable(createRippleColorStateList(), stateListDrawable, null)
        rippleDrawable
    &#125; else &#123;
        stateListDrawable
    &#125;
    setPadding(pL, pT, pR, pB)
&#125;


private fun createStateListDrawable(): StateListDrawable &#123;
    var normalDrawable = StateListDrawable()
    normalDrawable.addState(
            intArrayOf(android.R.attr.state_pressed),
            createPressedDrawable()
    )
    normalDrawable.addState(
            intArrayOf(android.R.attr.state_focused),
            createPressedDrawable()
    )
    normalDrawable.addState(
            intArrayOf(-android.R.attr.state_enabled),
            createDisableDrawable()
    )
    normalDrawable.addState(
            intArrayOf(android.R.attr.state_selected),
            createPressedDrawable()
    )
    normalDrawable.addState(intArrayOf(), createNormalDrawable())
    return normalDrawable
&#125;


private fun createRippleColorStateList(): ColorStateList &#123;
    val stateList = arrayOf(intArrayOf(android.R.attr.state_pressed), intArrayOf(android.R.attr.state_focused), intArrayOf(android.R.attr.state_activated), intArrayOf())
    val normalColor = backgroundStyle.getColorRippleNormalFallback()
    val pressedColor = backgroundStyle.getColorRipplePressedFallback()
    val stateColorList = intArrayOf(
            pressedColor,
            pressedColor,
            pressedColor,
            normalColor
    )
    return ColorStateList(stateList, stateColorList)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">第三步：UI组件实现</h5>
<p>xml中使用</p>
<pre><code class="copyable"><com.snapsolve.uikit.flatbutton.FlatButton
    app:fb_colorNormalText="@color/uikit_color_white"
    app:fb_colorPressedText="@color/uikit_color_white"
    app:fb_colorNormalEnd="#FF9800"
    app:fb_colorNormalStart="#FF0000"
    app:fb_colorPressedEnd="#4CAF50"
    app:fb_colorPressedStart="#009688"
    app:fb_colorRippleNormal="#303F9F"
    app:fb_colorRipplePressed="#FF4081"
    app:fb_cornerRadius="24dp"
    app:fb_gradientOrientation="left_right"
    app:fb_isRippleEnable="true" 
    ...
    />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中使用</p>
<pre><code class="copyable">fb_radius_in_code.setBackgroundStyle &#123;
    this.colorNormal = resources.getColor(R.color.uikit_color_FF4081)
    this.colorPressed = resources.getColor(R.color.uikit_color_9C27B0)
    this.colorRippleNormal = resources.getColor(R.color.uikit_color_FF4081)
    this.colorRipplePressed = resources.getColor(R.color.uikit_color_9C27B0)
&#125;.setRadiusStyle &#123;
    this.radiusTL = dp2px(24F)
    this.radius_BR = dp2px(24F)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，底层Button能力定义完成，接下来就是组件化实现了，具体实现方式如下：</p>
<p>无法复制加载中的内容</p>
<p>项目中的按钮UI按照UI组件要求，可以基于FlatButton来实现，配置好给种类型的属性，按钮名字可以和设计对齐，到这里就基本完成了</p>
<h5 data-id="heading-12">第四步：业务使用</h5>
<p>一级按钮、二级按钮、三级按钮的实现可以通过继承FlatButton，设置默认样式，使用的时候就不需要再在xml中定义任何属性，只需记住组件名字，依赖即可，做到真正的开箱即用</p>
<p>举一个例子，定义一个线框button</p>
<pre><code class="copyable">class StrokeButton : FlatButton &#123;
    constructor(context: Context) : this(context, null)
    constructor(context: Context, attrs: AttributeSet?) : this(context, attrs, 0)
    constructor(context: Context, attrs: AttributeSet?, defStyleAttr: Int) : super(context, attrs, defStyleAttr) &#123;
        config(context, attrs)
    &#125;

    private fun config(context: Context, attrs: AttributeSet?)&#123;
        .setBackgroundStyle &#123;
            this.colorNormal = resources.getColor(R.color.uikit_color_FF4081)
            this.colorPressed = resources.getColor(R.color.uikit_color_9C27B0)
            this.colorRippleNormal = resources.getColor(R.color.uikit_color_FF4081)
            this.colorRipplePressed = resources.getColor(R.color.uikit_color_9C27B0)
        &#125;.setRadiusStyle &#123;
            this.radiusTL = dp2px(28F)
            this.radius_BR = dp2px(28F)
        &#125;
    &#125;
    private fun dp2px(dp: Float): Float &#123;
        return TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, dp, resources.displayMetrics)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>业务使用</p>
<pre><code class="copyable"><com.snapsolve.uikit.demo.flatbutton.StrokeButton
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            