
---
title: '这15个Android开源库，只有经常逛Github的才知道！'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/3513995-2f3e154ec15d00f7.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/3513995-2f3e154ec15d00f7.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1000" data-height="500"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-2f3e154ec15d00f7.png" data-original-width="1000" data-original-height="500" data-original-format="image/png" data-original-filesize="53992" src="https://upload-images.jianshu.io/upload_images/3513995-2f3e154ec15d00f7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>哈喽，大家好，我是西哥！</p>
<p>又到了大家最喜欢了的环节--<strong>开源库推荐</strong>，前面为大家推荐了我收藏的一些非常酷的开源库，受到大家一致好评，还没看过的，请移步至：</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjuejin.im%2Fpost%2F6844903640927322126" target="_blank">【Android珍藏】推荐10个炫酷的开源库</a></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjuejin.im%2Fpost%2F6844903569120821262" target="_blank">【开源推荐】进阶实战，从一款音乐播放器开始</a></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjuejin.im%2Fpost%2F6844904138992517128" target="_blank">【2020年GitHub 上那些优秀Android开源库，这里是Top10！】</a></p>
<p>本期又为大家带来了哪些有趣的库呢？本期为大家精选了<code>15</code>个有趣又有用的开源，<code>排名不分先后</code>，一起来看看吧！</p>
<h3>1. Coil</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="400" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-94f852c6017c58d2.image" data-original-width="400" data-original-height="200" data-original-format="image/png" data-original-filesize="9463" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>Coil是Android上的一个全新的图片加载框架，它的全名叫做<code>coroutine image loader</code>,即协程图片加载库。与传统的图片加载库Glide，Picasso或Fresco等相比。该具有轻量（只有大约1500个方法）、快、易于使用、更现代的API等优势。</p>
<p>它支持GIF和SVG，并且可以执行四个默认转换：<code>模糊</code>，<code>圆形裁剪</code>，<code>灰度</code>和<code>圆角</code>。</p>
<p>示例如下：</p>
<pre><code class="kotlin">imageView.load(“https://www.example.com/image.jpg") &#123;
 crossfade(true)
 placeholder(R.drawable.image)
 transformations(CircleCropTransformation())
&#125;
</code></pre>
<p>并且是全用Kotlin编写，如果你是纯Kotlin项目的话，那么这个库应该是你的首选。</p>
<p>Github地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcoil-kt%2Fcoil" target="_blank">https://github.com/coil-kt/coil</a></p>
<h3>2. MultiSearchView</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="600"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-99598b1ee5333f17.image" data-original-width="800" data-original-height="600" data-original-format="image/gif" data-original-filesize="2569365" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>该库具有一个非常酷的<code>Search View</code>动画！</p>
<p>使用非常简单，并且可以自定义，你可以在在<code>styles.xml</code>下添加自定义样式。</p>
<p>示例代码：</p>
<pre><code class="xml"><com.iammert.library.ui.multisearchviewlib.MultiSearchView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>     
</code></pre>
<pre><code class="kotlin">multiSearchView.setSearchViewListener(object : MultiSearchView.MultiSearchViewListener&#123;
    override fun onItemSelected(index: Int, s: CharSequence) &#123;
    &#125;

    override fun onTextChanged(index: Int, s: CharSequence) &#123;
    &#125;

    override fun onSearchComplete(index: Int, s: CharSequence) &#123;
    &#125;

    override fun onSearchItemRemoved(index: Int) &#123;
    &#125;

&#125;)
</code></pre>
<p>自定义样式：</p>
<pre><code class="xml">  <!-- Search Text Style. -->
    <style name="SearchTextStyle">
        <!-- Custom values write to here for SearchEditText. -->
        <item name="android:focusable">true</item>
        <item name="android:focusableInTouchMode">true</item>
        <item name="android:enabled">true</item>
        <item name="android:hint">Search</item>
        <item name="android:imeOptions">actionSearch</item>
        <item name="android:textSize">18sp</item>
        <item name="android:maxLength">15</item>
        <item name="android:inputType">textCapSentences</item>
        <item name="android:textColorHint">#80999999</item>
        <item name="android:textColor">#000</item>
    </style>
</code></pre>
<p>然后，您应该将样式设置为<code>MultiSearchView</code>下的<code>app：searchTextStyle</code>。</p>
<p>Github地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fiammert%2FMultiSearchView" target="_blank">https://github.com/iammert/MultiSearchView</a></p>
<h3>3. CalendarView</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1400" data-height="455"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-50c2946513911c6f.image" data-original-width="1400" data-original-height="455" data-original-format="image/png" data-original-filesize="129510" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><code>CalendarView</code>是一个高度可定制化的日历组件库，用recycleView实现。</p>
<p>它有如下特性：</p>
<ul>
<li>单一或范围选择</li>
<li>周历或者月历模式</li>
<li>边界日期</li>
<li>自定义日历视图</li>
<li>水平或者垂直滚动模式</li>
<li>完全可定制的视图</li>
</ul>
<p>该库的文档也非常全面，并包含许多示例。此外，还有一个示例应用程序展示了库的所有功能。</p>
<p>它是用纯Kotlin编写的，并在MIT许可下发布。如果您需要在应用程序中使用日历视图，这是一个不错的选择。</p>
<blockquote>
<p>注意：该库通过Java 8+ API使用了java.time类，以便向后兼容，因为这些类是在Java 8中添加的。</p>
</blockquote>
<p>因此，需要在app的<code>build.gradle</code> 中添加如下配置：</p>
<pre><code class="java">android &#123;
  defaultConfig &#123;
    // Required ONLY when setting minSdkVersion to 20 or lower
    multiDexEnabled true
  &#125;

  compileOptions &#123;
    // Flag to enable support for the new language APIs
    coreLibraryDesugaringEnabled true
    // Sets Java compatibility to Java 8
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
  &#125;
&#125;

dependencies &#123;
  coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:<latest-version>'
&#125;
</code></pre>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fkizitonwose%2FCalendarView" target="_blank">https://github.com/kizitonwose/CalendarView</a></p>
<h3>4. Bubble Navigation</h3>
<table>
<thead>
<tr>
<th>FloatingTopBarActivity</th>
<th>TopBarActivity</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="504" data-height="896"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-349b60cab6c2873b.image" data-original-width="504" data-original-height="896" data-original-format="image/gif" data-original-filesize="343009" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div></td>
<td><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="504" data-height="896"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-19d5adb09505f4b0.image" data-original-width="504" data-original-height="896" data-original-format="image/gif" data-original-filesize="367148" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>BottomBarActivity</th>
<th>EqualBottomBarActivity</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="504" data-height="896"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-5cafe156faf6278d.image" data-original-width="504" data-original-height="896" data-original-format="image/gif" data-original-filesize="516603" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div></td>
<td><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="504" data-height="896"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-2068c38787b9d155.image" data-original-width="504" data-original-height="896" data-original-format="image/gif" data-original-filesize="344139" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div></td>
</tr>
</tbody>
</table>
<p><code>Bubble Navigation</code>是一个轻巧的库，可通过大量自定义选项轻松制作精美的导航栏。</p>
<p>它有很多非常的特性：</p>
<ul>
<li>
<p>针对不同用例的两种类型的<code>NavigationViews</code>：</p>
<ul>
<li><p><code>BubbleNavigationConstraintView</code>（支持spread<code>spread</code>，<code>inside</code>, 和 <code>packed</code>莫斯）</p></li>
<li><p><code>BubbleNavigationLinearView</code>（允许平均分配，使用权重或packed模式）</p></li>
</ul>
</li>
<li><p>高度可定制化</p></li>
<li><p>您可以添加小红点，它具有<code>BubbleToggleView</code>来创建新的UI组件，而不仅仅是导航</p></li>
</ul>
<p>示例：</p>
<pre><code class="xml"><com.gauravk.bubblenavigation.BubbleNavigationConstraintView
        android:id="@+id/top_navigation_constraint"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="380dp"
        android:background="@color/white"
        android:elevation="4dp"
        android:padding="12dp"
        app:bnc_mode="spread">

        <com.gauravk.bubblenavigation.BubbleToggleView
            android:id="@+id/c_item_rest"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            app:bt_active="true"
            app:bt_colorActive="@color/search_active"
            app:bt_colorInactive="@color/search_inactive"
            app:bt_icon="@drawable/ic_restaurant"
            app:bt_shape="@drawable/transition_background_drawable_restaurant"
            app:bt_title="@string/restaurant"
            app:bt_padding="@dimen/internal_padding"
            app:bt_titlePadding="@dimen/title_padding" />

         <!-- Add more child items here - max upto 5 -->
    
    </com.gauravk.bubblenavigation.BubbleNavigationConstraintView>
</code></pre>
<p>Github文档很完善，有很多示例，更多用法和属性可去Github了解。</p>
<p>Github:<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fgauravk95%2Fbubble-navigation" target="_blank">https://github.com/gauravk95/bubble-navigation</a></p>
<h3>5. FabFilter</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="640" data-height="640"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-d5a59b917f97c4d5.image" data-original-width="640" data-original-height="640" data-original-format="image/gif" data-original-filesize="3429101" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>这是一个有趣的项目，它不是一个直接可用的库，而是一个示例应用程序，展示了<code>使用</code>和<code>不使用</code> <code>MotionLayout</code>两种方式来实现的高级UI动画。</p>
<p>详细的实现细节可以看看Medium上的系列文章：</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fproandroiddev.com%2Fcomplex-ui-animation-on-android-8f7a46f4aec4" target="_blank">“Complex UI/Animations on Android”</a></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fproandroiddev.com%2Fcomplex-ui-animations-on-android-featuring-motionlayout-aa82d83b8660" target="_blank">“Complex UI/Animations on Android — featuring MotionLayout”</a></p>
<p>Github:<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fnikhilpanju%2FFabFilter" target="_blank">https://github.com/nikhilpanju/FabFilter</a></p>
<h3>6.android-showcase</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="336" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-c1fb3b7b76149eab.image" data-original-width="336" data-original-height="596" data-original-format="image/gif" data-original-filesize="1839026" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><code>android-showcase</code>是一个非常优秀的开源项目，它是一个展示应用程序，展示了如何使用Kotlin和最新的Jetpack 技术栈来开发一个APP。</p>
<p>该项目为您带来了一系列最佳实践，工具和解决方案：</p>
<ul>
<li>100% Kotlin</li>
<li>现代架构 (feature modules, clean architecture, Model-View-ViewModel, Model-View-Intent)</li>
<li>Android Jetpack组件</li>
<li>单Activity模式，使用Navigation导航</li>
</ul>
<p>看完这个项目，在模块化，Clean体系结构，测试、设置CI / CD工具，等方面，你将会受到启发。感谢作者的开源。</p>
<p>Github：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Figorwojda%2Fandroid-showcase" target="_blank">https://github.com/igorwojda/android-showcase</a></p>
<h3>7. Croppy</h3>
<p>[图片上传失败...(image-cf4104-1596436309874)]</p>
<p><code>Croppy</code>是一个Android图片裁剪库。</p>
<p>它有很多强大的特性：</p>
<ul>
<li>双指缩放</li>
<li>裁剪任意大小</li>
<li>按照长宽比例裁剪</li>
<li>显示裁剪后的Bitmap</li>
<li>自动居中裁剪</li>
<li>全面的动画使用体验</li>
</ul>
<p>更多使用细节请看Github。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Flyrebirdstudio%2FCroppy" target="_blank">https://github.com/lyrebirdstudio/Croppy</a></p>
<h3>8. RubberPicker</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="514" data-height="506"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-46a5b1c894c5d8b2.image" data-original-width="514" data-original-height="506" data-original-format="image/gif" data-original-filesize="4407489" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>一个炫酷的、有趣的SeekBar动画库。</p>
<p><code>RubberPicker</code>库包含<code>RubberSeekBar</code>和<code>RubberRangePicker</code>，其灵感来自<code>Cuberto</code>的<code>iOS橡胶范围选择器</code>。</p>
<p>使用示例：</p>
<p>布局文件中配置</p>
<pre><code class="xml"><com.jem.rubberpicker.RubberSeekBar
  ...
  app:minValue="20"
  app:maxValue="80"
  app:elasticBehavior="cubic"
  app:dampingRatio="0.3"
  app:stiffness="300"
  app:stretchRange="24dp"
  app:defaultThumbRadius="16dp"
  app:normalTrackWidth="4dp"
  app:highlightTrackWidth="8dp"
  app:normalTrackColor="#AAAAAA"
  app:highlightTrackColor="#BA1F33"
  app:defaultThumbInsideColor="#FFF"
  app:highlightDefaultThumbOnTouchColor="#CD5D67"/>

<!-- Similar attributes can be applied for RubberRangePicker as well-->
<com.jem.rubberpicker.RubberRangePicker
  ...
  app:minValue="0"
  app:maxValue="100"
  app:elasticBehavior="linear"
  app:dampingRatio="0.4"
  app:stiffness="400"
  app:stretchRange="36dp"
  app:defaultThumbRadius="16dp"
  app:normalTrackWidth="4dp"
  app:highlightTrackWidth="8dp"
  app:normalTrackColor="#AAAAAA"
  app:highlightTrackColor="#BA1F33"
  app:defaultThumbInsideColor="#CFCD5D67"
  app:highlightDefaultThumbOnTouchColor="#CD5D67"/>
</code></pre>
<p>或者，在代码中动态配置：</p>
<pre><code class="kotlin">val rubberSeekBar = RubberSeekBar(this)
rubberSeekBar.setMin(20)
rubberSeekBar.setMax(80)
rubberSeekBar.setElasticBehavior(ElasticBehavior.CUBIC)
rubberSeekBar.setDampingRatio(0.4F)
rubberSeekBar.setStiffness(1000F)
rubberSeekBar.setStretchRange(50f)
rubberSeekBar.setThumbRadius(32f)
rubberSeekBar.setNormalTrackWidth(2f)
rubberSeekBar.setHighlightTrackWidth(4f)
rubberSeekBar.setNormalTrackColor(Color.GRAY)
rubberSeekBar.setHighlightTrackColor(Color.BLUE)
rubberSeekBar.setHighlightThumbOnTouchColor(Color.CYAN)
rubberSeekBar.setDefaultThumbInsideColor(Color.WHITE)

val currentValue = rubberSeekBar.getCurrentValue()
rubberSeekBar.setCurrentValue(currentValue + 10)
rubberSeekBar.setOnRubberSeekBarChangeListener(object : RubberSeekBar.OnRubberSeekBarChangeListener &#123;
    override fun onProgressChanged(seekBar: RubberSeekBar, value: Int, fromUser: Boolean) &#123;&#125;
    override fun onStartTrackingTouch(seekBar: RubberSeekBar) &#123;&#125;
    override fun onStopTrackingTouch(seekBar: RubberSeekBar) &#123;&#125;
&#125;)


//Similarly for RubberRangePicker
val rubberRangePicker = RubberRangePicker(this)
rubberRangePicker.setMin(20)
...
rubberRangePicker.setHighlightThumbOnTouchColor(Color.CYAN)

val startThumbValue = rubberRangePicker.getCurrentStartValue()
rubberRangePicker.setCurrentStartValue(startThumbValue + 10)
val endThumbValue = rubberRangePicker.getCurrentEndValue()
rubberRangePicker.setCurrentEndValue(endThumbValue + 10)
rubberRangePicker.setOnRubberRangePickerChangeListener(object: RubberRangePicker.OnRubberRangePickerChangeListener&#123;
    override fun onProgressChanged(rangePicker: RubberRangePicker, startValue: Int, endValue: Int, fromUser: Boolean) &#123;&#125;
    override fun onStartTrackingTouch(rangePicker: RubberRangePicker, isStartThumb: Boolean) &#123;&#125;
    override fun onStopTrackingTouch(rangePicker: RubberRangePicker, isStartThumb: Boolean) &#123;&#125;
&#125;)
</code></pre>
<p>更多、更详细的使用请看Github。</p>
<p>Github：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FChrisvin%2FRubberPicker" target="_blank">https://github.com/Chrisvin/RubberPicker</a></p>
<h3>9. Switcher</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="400" data-height="600"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-6d2a308854ef50f5.image" data-original-width="400" data-original-height="600" data-original-format="image/gif" data-original-filesize="1018381" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>一个炫酷的Switcher 切换动画库，真是的太可爱了，我前面也写过文章专门介绍过：</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjuejin.im%2Fpost%2F6844904088174329864" target="_blank">炫酷！从未见过如此Q弹的Switcher</a></p>
<p>它的灵感来自于 Dribble上<code>Oleg Frolov</code>的设计。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fbitvale%2FSwitcher" target="_blank">https://github.com/bitvale/Switcher</a></p>
<h3>10. StfalconImageViewer</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="270" data-height="480"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-8613206586ec9b32.image" data-original-width="270" data-original-height="480" data-original-format="image/gif" data-original-filesize="4933133" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><code>StfalconImageViewer</code>是一个图片查看库，<br>
该库简单且可定制。它包含一个<code>全屏图像查看器</code>，<strong>具有共享的图像过渡支持</strong>，<code>捏合缩放功能</code>以及<code>滑动手势来关闭</code>手势。</p>
<p>Github文档说明了如何使用每个功能。同样值得注意的是：该库与所有最受欢迎的图像处理库（例如Picasso，Glide等）兼容。</p>
<p>所有可配置项如下：</p>
<pre><code class="kotlin">StfalconImageViewer.Builder<String>(this, images, ::loadImage)
            .withStartPosition(startPosition)
            .withBackgroundColor(color)
            //.withBackgroundColorResource(R.color.color)
            .withOverlayView(view)
            .withImagesMargin(R.dimen.margin)
            //.withImageMarginPixels(margin)
            .withContainerPadding(R.dimen.padding)
            //.withContainerPadding(R.dimen.paddingStart, R.dimen.paddingTop, R.dimen.paddingEnd, R.dimen.paddingBottom)
            //.withContainerPaddingPixels(padding)
            //.withContainerPaddingPixels(paddingStart, paddingTop, paddingEnd, paddingBottom)
            .withHiddenStatusBar(shouldHideStatusBar)
            .allowZooming(isZoomingAllowed)
            .allowSwipeToDismiss(isSwipeToDismissAllowed)
            .withTransitionFrom(targeImageView)
            .withImageChangeListener(::onImageChanged)
            .withDismissListener(::onViewerDismissed)
            .withDismissListener(::onViewerDismissed)
</code></pre>
<p>更详细的使用请看Github。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fstfalcon-studio%2FStfalconImageViewer" target="_blank">https://github.com/stfalcon-studio/StfalconImageViewer</a></p>
<h3>11. Broccoli</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="270" data-height="480"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-523d8be30033ebad.image" data-original-width="270" data-original-height="480" data-original-format="image/gif" data-original-filesize="629319" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><code>Broccoli</code>是一个show View Loading 库，也就是我常说的<strong>骨架屏</strong>，在内容加载的时候，显示一个占位符。</p>
<p>该库带有很平滑的动画效果，你可以配合RecyclerView一起使用，等待加载内容时，再也不枯燥了。</p>
<p>示例：</p>
<pre><code class="java">Broccoli broccoli = new Broccoli();

//add the default style placeholder
broccoli.addPlaceholders('activity', 'view_id', 'view_id'); 

or 
//add the default style placeholder
broccoli.addPlaceholders('view1', 'view2', 'view3'); 

or 

//add the custom style placeholder
broccoli.addPlaceholder(new PlaceholderParameter.Builder()
                        .setView('view')
                        .setAnimation('scaleAnimation');
                        .setDrawable(DrawableUtils.createRectangleDrawable(placeHolderColor, 0))
                        .build()); 

or
//add the custom style placeholder with gradient animation
broccoli.addPlaceholder(new PlaceholderParameter.Builder()
                        .setView('view')
                        .setDrawable(new BroccoliGradientDrawable(Color.parseColor("#DDDDDD"),
                            Color.parseColor("#CCCCCC"), 0, 1000, new LinearInterpolator())
                        .build()); 
broccoli.show();
</code></pre>
<p>更多使用请看Github。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fsamlss%2FBroccoli" target="_blank">https://github.com/samlss/Broccoli</a></p>
<h3>12. Orbit MVI</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="752" data-height="502"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-4a9aa6eba685cd4d.image" data-original-width="752" data-original-height="502" data-original-format="image/png" data-original-filesize="34183" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>这是一个用于Kotlin和Android的Model-View-Intent （MVI）框架。它的灵感来自Jake Wharton，RxFeedback和Mosby的“Managing State with RxJava”。</p>
<p>根据ReadMe所说：</p>
<blockquote>
<p>Orbit在您的redux实现周围提供了尽可能小的结构，以使其易于使用，但您仍可以使用RxJava的强大功能。</p>
</blockquote>
<p>redux系统可能如下所示：</p>
<pre><code class="kotlin">data class State(val total: Int = 0)

data class AddAction(val number: Int)

sealed class SideEffect &#123;
    data class Toast(val text: String) : SideEffect()
&#125;

class CalculatorViewModel : OrbitViewModel<State, SideEffect> (State(), &#123;

    perform("addition")
        .on<AddAction>()
        .sideEffect &#123; post(SideEffect.Toast("Adding $&#123;event.number&#125;")) &#125;
        .reduce &#123;
            currentState.copy(currentState.total + event.number)
        &#125;

    ...
&#125;)
</code></pre>
<p>activity / fragment 中：</p>
<pre><code class="kotlin">// Example of injection using koin, your DI system might differ
private val viewModel by viewModel<CalculatorViewModel>()

override fun onCreate() &#123;
    ...
    addButton.setOnClickListener &#123; viewModel.sendAction(AddAction) &#125;
&#125;

override fun onStart() &#123;
    viewModel.connect(this, ::handleState, ::handleSideEffect)
&#125;

private fun handleState(state: State) &#123;
    ...
&#125;

private fun handleSideEffect(sideEffect: SideEffect) &#123;
    when (sideEffect) &#123;
        is SideEffect.Toast -> toast(sideEffect.text)
    &#125;
&#125;
</code></pre>
<p>详细使用请看Github。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fbabylonhealth%2Forbit-mvi" target="_blank">https://github.com/babylonhealth/orbit-mvi</a></p>
<h3>13. IndicatorScrollView</h3>
<table>
<thead>
<tr>
<th>IndicatorScrollView</th>
<th>IndicatorScrollView</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="337" data-height="607"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-bc19b27fe58bd9ba.image" data-original-width="337" data-original-height="607" data-original-format="image/gif" data-original-filesize="9757616" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div></td>
<td><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="337" data-height="607"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-2984e9cadf7df0dd.image" data-original-width="337" data-original-height="607" data-original-format="image/gif" data-original-filesize="5052222" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div></td>
</tr>
</tbody>
</table>
<p>该库为<code>NestedScrollView</code>添加了逻辑，使它可以在滚动时，更改对指示器进行动态响应。</p>
<p>README文件包含开始项目所需的所有信息，例如如何使用<code>IndicatorScrollView</code>，<code>IndicatorView</code>和<code>IndicatorItem</code>。目前,它的版本为<code>1.0.2</code>，是根据Apache 2.0许可发布的。它支持API 16及更高版本。</p>
<p>文档示例很详细，更多使用相关请看Github。</p>
<p>Github： <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fskydoves%2FIndicatorScrollView" target="_blank">https://github.com/skydoves/IndicatorScrollView</a></p>
<h3>14. Cyanea</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="300" data-height="533"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-b5f0145c88275ba4.image" data-original-width="300" data-original-height="533" data-original-format="image/gif" data-original-filesize="278806" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><code>Cyanea</code> 是一个Android 主题引擎库。</p>
<p>它允许那你动态更换应用主题，它内置了很多主题如：</p>
<ul>
<li><code>Theme.Cyanea.Dark</code></li>
<li><code>Theme.Cyanea.Dark.LightActionBar</code></li>
<li><code>Theme.Cyanea.Dark.NoActionBar</code></li>
<li><code>Theme.Cyanea.Light</code></li>
<li><code>Theme.Cyanea.Light.DarkActionBar</code></li>
<li><code>Theme.Cyanea.Light.NoActionBar</code></li>
</ul>
<p>更多详细信息请看Github。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fjaredrummler%2FCyanea" target="_blank">https://github.com/jaredrummler/Cyanea</a></p>
<h3>15. Android MotionLayout Carousel</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="270" data-height="480"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-4590e66d08bebf70.image" data-original-width="270" data-original-height="480" data-original-format="image/gif" data-original-filesize="1642466" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>这是一个示例项目，它展示了如何使用<code>MotionLayout</code>来实现一个炫酷的轮播图。</p>
<p>文档几乎没有任何说明，但是如果你最近也在探索MotionLayout，这将是一个很好示例。</p>
<p>Github: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Ffaob-dev%2FMotionLayoutCarousel" target="_blank">https://github.com/faob-dev/MotionLayoutCarousel</a></p>
<h3>总结</h3>
<p>以上就是本期的开源项目推荐，如果你也有好玩的、有趣的、强大的开源项目，也可以推荐给西哥，欢迎评论区留言讨论。</p>
<blockquote>
<p>文章首发于公众号：<code>「 技术最TOP 」</code>，每天都有干货文章持续更新，可以微信搜索<code>「 技术最TOP 」</code>第一时间阅读，回复【思维导图】【面试】【简历】有我准备一些Android进阶路线、面试指导和简历模板送给你</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="900" data-height="500"><img data-original-src="//upload-images.jianshu.io/upload_images/3513995-aab4ea100ca2f605" data-original-width="900" data-original-height="500" data-original-format="image/png" data-original-filesize="439754" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
  
</div>
            