
---
title: '让 Flutter 在鸿蒙系统上跑起来'
categories: 
 - 博客
 - 美团技术团队
 - — 最近更新
headimg: 'https://p0.meituan.net/travelcube/82c25693219162957568b36adc96c2a6234729.png'
author: 美团技术团队
comments: false
date: Fri, 22 Jan 2021 00:00:00 GMT
thumbnail: 'https://p0.meituan.net/travelcube/82c25693219162957568b36adc96c2a6234729.png'
---

<div>   
<h2 id="前言">前言</h2><p><strong>鸿蒙系统</strong> （HarmonyOS）是华为推出的一款面向未来、面向全场景的分布式操作系统。在传统单设备系统能力的基础上，鸿蒙提出了基于同一套系统能力、适配多种终端形态的分布式理念。自 2020 年 9 月 HarmonyOS 2.0 发布以来，华为加快了鸿蒙系统大规模落地的步伐，预计 2021 年底，鸿蒙系统会覆盖包括手机、平板、智能穿戴、智慧屏、车机在内数亿台终端设备。对移动应用而言，<strong>新的系统理念、新的交互形式，也意味着新的机遇</strong>。如果能够利用好鸿蒙的开发生态及其特性能力，可以让应用覆盖更多的交互场景和设备类型，从而带来新的增长点。</p><p>与面临的机遇相比，适配鸿蒙系统带来的挑战同样巨大。当前手机端，尽管鸿蒙系统仍然支持安卓 APK 安装及运行，但长期来看，华为势必会抛弃 AOSP，逐步发展出自己的生态，这意味着现有安卓应用在鸿蒙设备上将会逐渐变成“二等公民”。然而，如果在 iOS 及 Android 之外再重新开发和维护一套鸿蒙应用，在如今业界越来越注重开发迭代效率的环境下，所带来的开发成本也是难以估量的。因此，通过打造一套合适的跨端框架，以相对低的成本移植应用到鸿蒙平台，并利用好该系统的特性能力，就成为了一个非常重要的选项。</p><p>在现有的众多跨端框架当中，Flutter 以其自渲染能力带来的多端高度一致性，在新系统的适配上有着突出的优势。虽然Flutter 官方<a href="https://github.com/flutter/flutter/issues/38437">并没有适配鸿蒙的计划</a>，但经过一段时间的探索和实践，美团外卖 MTFlutter 团队成功实现了 Flutter 对于鸿蒙系统的原生支持。</p><p>这里也要提前说明一下，因为鸿蒙系统目前还处于Beta版本，所以这套适配方案还没有在实际业务中上线，属于技术层面比较前期的探索。接下来本文会通过原理和部分实现细节的介绍，分享我们在移植和开发过程中的一些经验。希望能对大家有所启发或者帮助。</p><h2 id="背景知识和基础概念介绍">背景知识和基础概念介绍</h2><p>在适配开始之前，我们要明确好先做哪些事情。先来回顾一下 Flutter 的三层结构：</p><p><img src="https://p0.meituan.net/travelcube/82c25693219162957568b36adc96c2a6234729.png" alt referrerpolicy="no-referrer"></p><p>在 Flutter 的架构设计中，最上层为<strong>框架层</strong>，使用 Dart 语言开发，面向 Flutter 业务的开发者；中间层为<strong>引擎层</strong>，使用 C/C++ 开发，实现了 Flutter 的渲染管线和 Dart 运行时等基础能力；最下层为<strong>嵌入层</strong>，负责与平台相关的能力实现。显然我们要做的是将嵌入层移植到鸿蒙上，确切地说，我们要<strong>通过鸿蒙原生提供的平台能力，重新实现一遍 Flutter 嵌入层</strong>。</p><p>对于 Flutter 嵌入层的适配，Flutter 官方有一份不算详细的<a href="https://github.com/flutter/flutter/wiki/Custom-Flutter-Engine-Embedders">指南</a>，实际操作起来成本很高。由于鸿蒙的业务开发语言仍然可用 Java，在很多基础概念上与 Android 也有相似之处（如下表所示），我们可以从 Android 的实现入手，完成对鸿蒙的移植。</p><p><img src="https://p0.meituan.net/travelcube/92d1c25f2d12f3cdd995f55d774d9bdf509435.png" alt referrerpolicy="no-referrer"></p><h2 id="flutter-在鸿蒙上的适配">Flutter 在鸿蒙上的适配</h2><p>如前文所述，要完成 Flutter 在新系统上的移植，我们需要完整实现 Flutter 嵌入层要求的所有子模块，而从能力支持角度，<strong>渲染</strong>、<strong>交互</strong>以及<strong>其他必要的原生平台能力</strong>是保证 Flutter 应用能够运行起来的最基本的要素，需要优先支持。接下来会依次进行介绍。</p><h3 id="1-渲染流程打通">1. 渲染流程打通</h3><p>我们再来回顾一下 Flutter 的图像渲染流程。如图所示，设备发起<strong>垂直同步</strong>（VSync）信号之后，先经过 UI 线程的渲染管线（Animate/Build/Layout/Paint），再经过 Raster 线程的组合和栅格化，最终通过 OpenGL 或 Vulkan 将图像<strong>上屏</strong>。这个流程的大部分工作都由框架层和引擎层完成，对于鸿蒙的适配，我们主要关注的是与设备自身能力相关的问题，即：</p><p>(1) 如何监听设备的 VSync 信号并通知 Flutter 引擎？
(2) OpenGL/Vulkan 用于上屏的窗口对象从何而来？</p><p><img src="https://p1.meituan.net/travelcube/8445f566ade9fc155a9e0652bc9bca70117066.png" alt referrerpolicy="no-referrer"></p><p><strong>VSync 信号的监听及传递</strong></p><p>在 Flutter 引擎的 Android 实现中，设备的 VSync 信号通过 <a href="https://developer.android.com/reference/android/view/Choreographer">Choreographer</a> 触发，它产生及消费流程如下图所示：</p><p><img src="https://p1.meituan.net/travelcube/bbaa255fb1c4e609342b771558bd39c7143339.png" alt="Flutter VSync" referrerpolicy="no-referrer"></p><p>Flutter 框架注册 VSync 回调之后，通过 C++ 侧的 VsyncWaiter 类等待 VSync 信号，后者通过 JNI 等一系列调用，最终 Java 侧的 VsyncWaiter 类调用 Android SDK 的 <a href="https://developer.android.com/reference/android/view/Choreographer#postFrameCallback(android.view.Choreographer.FrameCallback)">Choreographer.postFrameCallback</a> 方法，再通过 JNI 一层层传回 Flutter 引擎消费掉此回调。Java 侧的 VsyncWaiter 核心代码如下：</p><pre><code class="language-java">@Override
public void asyncWaitForVsync(long cookie) &#123;
  Choreographer.getInstance()
      .postFrameCallback(
        new Choreographer.FrameCallback() &#123;
          @Override
          public void doFrame(long frameTimeNanos) &#123;
            float fps = windowManager.getDefaultDisplay().getRefreshRate();
            long refreshPeriodNanos = (long) (1000000000.0 / fps);
            FlutterJNI.nativeOnVsync(
              frameTimeNanos, frameTimeNanos + refreshPeriodNanos, cookie);
          &#125;
        &#125;);
&#125;
</code></pre><p>在整个流程中，除了来自 Android SDK 的 Choreographer 以外，大多数逻辑几乎都由 C++ 和 Java 的基础 SDK 实现，可以直接在鸿蒙上复用，问题是鸿蒙目前的 API 文档中尚没有开放类似 Choreographer 的能力。所以现阶段我们可以借用鸿蒙提供的类似 iOS <a href="https://developer.apple.com/documentation/DISPATCH">Grand Central Dispatch</a> 的线程 API，模拟出 VSync 的信号触发与回调：</p><pre><code class="language-java">@Override
public void asyncWaitForVsync(long cookie) &#123;
  // 模拟每秒 60 帧的屏幕刷新间隔：向主线程发送一个异步任务, 16ms 后调用
  applicationContext.getUITaskDispatcher().delayDispatch(() -> &#123;
    float fps = 60; // 设备刷新帧率，HarmonyOS 未暴露获取帧率 API，先写死 60 帧
    long refreshPeriodNanos = (long) (1000000000.0 / fps);
    long frameTimeNanos = System.nanoTime();
    FlutterJNI.nativeOnVsync(frameTimeNanos, frameTimeNanos + refreshPeriodNanos, cookie);
  &#125;, 16);
&#125;;
</code></pre><p><strong>渲染窗口的构建及传递</strong></p><p>在这一部分，我们需要在鸿蒙系统上构建平台容器，为 Flutter 引擎的图形渲染提供用于上屏的窗口对象。同样，我们参考 Flutter for Android 的实现，看一下 Android 系统是怎么做的：</p><p><img src="https://p0.meituan.net/travelcube/aaab9fdc5bc3fa4ef41643c5e53c87c8159860.png" alt referrerpolicy="no-referrer"></p><p>Flutter 在 Android 上支持 Vulkan 和 OpenGL 两种渲染引擎，篇幅原因我们只关注 OpenGL。抛开复杂的注册及调用细节，本质上整个流程主要做了三件事：</p><ol><li>创建了一个<strong>视图对象</strong>，提供可用于直接绘制的 Surface，将它通过 JNI 传递给原生侧；</li><li>在原生侧获取 Surface 关联的<strong>本地窗口对象</strong>，并交给 Flutter 的平台容器；</li><li>将本地窗口对象转换为 OpenGL ES 可识别的<strong>绘图表面（EGLSurface）</strong>，用于 Flutter 引擎的渲染上屏。</li></ol><p>接下来我们用鸿蒙提供的平台能力实现这三点。</p><p><strong>a. 可用于直接绘制的视图对象</strong></p><p>鸿蒙系统的 UI 框架<a href="https://developer.harmonyos.com/cn/docs/documentation/doc-guides/ui-java-overview-0000000000500404">提供了很多常用视图组件（Component）</a>，比如按钮、文字、图片、列表等，但我们需要抛开这些上层组件，获得直接绘制的能力。借助官方 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-guides/tv-media-playback-0000001050714866">媒体播放器开发指导</a> 文档，可以发现鸿蒙提供了 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/surfaceprovider-0000001054358716">SurfaceProvider</a> 类，它管理的 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/surface-0000001054120059">Surface</a> 对象可以用于视频解码后的展示。而 Flutter 渲染与视频上屏从原理上是类似的，因此我们可以借用 SurfaceProvider 实现 Surface 的管理和创建：</p><pre><code class="language-java">// 创建一个用于管理 Surface 的容器组件
SurfaceProvider surfaceProvider = new SurfaceProvider(context);
// 注册视图创建回调
surfaceProvider.getSurfaceOps().get().addCallback(surfaceCallback);

// ... 在 surfaceCallback 中
@Override
public void surfaceCreated(SurfaceOps surfaceOps) &#123;
  Surface surface = surfaceOps.getSurface();
  // ...将 surface 通过 JNI 交给 Native 侧
  FlutterJNI.onSurfaceCreated(surface);
&#125;
</code></pre><p><strong>b. 与 Surface 关联的本地窗口对象</strong></p><p>鸿蒙目前开放的 Native API 并不多，在官方文档中我们可以比较容易地找到 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/native__layer-0000001060033509">Native_layer API</a>。根据文档的说明，Native API 中的 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/native__layer-0000001060033509#EN-US_TOPIC_0000001060033509__ga10f0496160a17e00453c6744fb98a3f6">NativeLayer</a> 对象刚好对应了 Java 侧的 Surface 类，借助 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/native__layer-0000001060033509#EN-US_TOPIC_0000001060033509__ga10f0496160a17e00453c6744fb98a3f6">GetNativeLayer</a> 方法，我们实现了两者之间的转化：</p><pre><code class="language-c++">// platform_view_android_jni_impl.cc
static void SurfaceCreated(JNIEnv* env, jobject jcaller, jlong shell_holder, jobject jsurface) &#123;
  fml::jni::ScopedJavaLocalFrame scoped_local_reference_frame(env);
  // 通过鸿蒙 Native API 获取本地窗口对象 NativeLayer
  auto window = fml::MakeRefCounted<AndroidNativeWindow>(
      GetNativeLayer(env, jsurface));
  ANDROID_SHELL_HOLDER->GetPlatformView()->NotifyCreated(std::move(window));
&#125;
</code></pre><p><strong>c. 与本地窗口对象关联的 EGLSurface</strong></p><p>在 Android 的 <a href="https://source.android.google.cn/devices/graphics/arch-egl-opengl?hl=zh-cn">AOSP 实现</a>中，EGLSurface 可通过 EGL 库的 <a href="https://www.khronos.org/registry/EGL/sdk/docs/man/html/eglCreateWindowSurface.xhtml">eglCreateWindowSurface</a> 方法从本地窗口对象 <strong>ANativeWindow</strong> 创建而来。对于鸿蒙而言，虽然我们没有从公开文档找到类似的说明，但是 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/library-0000001060513586">鸿蒙标准库</a> 默认支持了 OpenGL ES，而且鸿蒙 SDK 中也附带了 EGL 相关的库及头文件，我们有理由相信在鸿蒙系统上，EGLSurface 也可以通过此方法从前一步生成的 <strong>NativeLayer</strong> 转化而来，在之后的验证中我们也确认了这一点：</p><pre><code class="language-c++">// window->handle() 即为之前得到的 NativeLayer
EGLSurface surface = eglCreateWindowSurface(
      display, config_, reinterpret_cast<EGLNativeWindowType>(window->handle()),
      attribs);
//...交给 Flutter 渲染管线
</code></pre><h3 id="2-交互能力实现">2. 交互能力实现</h3><p><strong>交互能力</strong>是支撑 Flutter 应用能够正常运行的另一个基本要求。在 Flutter 中，交互包含了各种触摸事件、鼠标事件、键盘录入事件的传递及消费。以触摸事件为例，Flutter 事件传递的整个流程如下图所示：</p><p><img src="https://p0.meituan.net/travelcube/0ad0faaed6c09b3ad1b66c3a496a269b245453.png" alt="Flutter 事件分发" referrerpolicy="no-referrer"></p><p>iOS/Android 的原生容器通过触摸事件的回调 API 接收到事件之后，会将其打包传递至引擎层，后者将事件传发给 Flutter 框架层，并完成事件的消费、分发和逻辑处理。同样，整个流程的大部分工作已经由 Flutter 统一，我们要做的仅仅是在原生容器上<strong>监听</strong>用户的输入，并<strong>封装</strong>成指定格式交给引擎层而已。</p><p>在鸿蒙系统上，我们可以借助平台提供的 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-guides/ui-multimodal-overview-0000000000031876">多模输入 API</a>，实现多种类型事件的监听：</p><pre><code class="language-java">flutterComponent.setTouchEventListener(touchEventListener); // 触摸及鼠标事件
flutterComponent.setKeyEventListener(keyEventListener); // 键盘录入事件
flutterComponent.setSpeechEventListener(speechEventListener); // 语音录入事件
</code></pre><p>对于事件的封装处理，可以复用 Android 已有逻辑，只需要关注鸿蒙与 Android 在事件处理上的对应关系即可，比如触摸事件的部分对应关系：</p><p><img src="https://p1.meituan.net/travelcube/6ebd5bcec043465e77669e24bca1c250240825.png" alt referrerpolicy="no-referrer"></p><h3 id="3-其他必要的平台能力">3. 其他必要的平台能力</h3><p>为了保证 Flutter 应用能够正常运行，除了最基本的渲染和交互外，我们的嵌入层还要提供资源管理、事件循环、生命周期同步等平台能力。对于这些能力 Flutter 大多都在嵌入层的公共部分有抽象类声明，只需要使用鸿蒙 API 重新实现一遍即可。</p><p>比如资源管理，引擎提供了 <a href="https://github.com/flutter/engine/blob/master/assets/asset_resolver.h">AssetResolver</a> 声明，我们可以使用鸿蒙 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/rawfile-0000001061151248">Rawfile</a> API 来实现：</p><pre><code class="language-c++">class HAPAssetMapping : public fml::Mapping &#123;
 public:
  HAPAssetMapping(RawFile* asset) : asset_(asset) &#123;&#125;
  ~HAPAssetMapping() override &#123; CloseRawFile(asset_); &#125;

  size_t GetSize() const override &#123; return GetRawFileSize(asset_); &#125;

  const uint8_t* GetMapping() const override &#123;
    return reinterpret_cast<const uint8_t*>(GetRawFileBuffer(asset_));
  &#125;

 private:
  RawFile* const asset_;

  FML_DISALLOW_COPY_AND_ASSIGN(HAPAssetMapping);
&#125;;
</code></pre><p>对于事件循环，引擎提供了 <a href="https://github.com/flutter/engine/blob/master/fml/message_loop_impl.h">MessageLoopImpl</a> 抽象类，我们可以使用鸿蒙 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-references/native__eventhandler-0000001054795159">Native_EventHandler</a> API 实现：</p><pre><code class="language-c++">// runner_ 为鸿蒙 EventRunnerNativeImplement 的实例
void MessageLoopHarmony::Run() &#123;
  FML_DCHECK(runner_ == GetEventRunnerNativeObjForThread());
  int result = ::EventRunnerRun(runner_);
  FML_DCHECK(result == 0);
&#125;

void MessageLoopHarmony::Terminate() &#123;
  int result = ::EventRunnerStop(runner_);
  FML_DCHECK(result == 0);
&#125;
</code></pre><p>对于生命周期的同步，鸿蒙的 <a href="https://developer.harmonyos.com/cn/docs/documentation/doc-guides/ability-page-concept-0000000000033573">Page Ability</a> 提供了完整的生命周期回调（如下图所示），我们只需要在对应的时机将状态上报给引擎即可。</p><p><img src="https://p0.meituan.net/travelcube/7a5c0c3b6bb517b494f56e39cac9421c50304.png" alt="Page Ability Lifecycle" referrerpolicy="no-referrer"></p><p>当以上这些能力都准备好之后，我们就可以成功把 Flutter 应用跑起来了。以下是通过 <a href="https://developer.harmonyos.com/cn/develop/deveco-studio">DevEco Studio</a> 运行官方 <a href="https://github.com/flutter/gallery">flutter gallery</a> 应用的截图，截图中 Flutter 引擎已经使用鸿蒙系统的平台能力进行了重写：</p><p><img src="https://p1.meituan.net/travelcube/3344307a5513c6b345f4af8962fc0ab3798292.png" alt="DevEco Running Flutte" referrerpolicy="no-referrer"></p><p>借由鸿蒙的多设备支持能力，此应用甚至可在 TV、车机、手表、平板等设备上运行：</p><p><img src="https://p0.meituan.net/travelcube/c8257b6607215e1f6916b11e171d84e6262859.jpg" alt="Flutter Multiple Devices" referrerpolicy="no-referrer"></p><h2 id="总结和展望">总结和展望</h2><p>通过上述的构建和适配工作，我们以极小的开发成本实现了 Flutter 在鸿蒙系统上的移植，基于 Flutter 开发的上层业务几乎不做任何修改就可以在鸿蒙系统上原生运行，为迎接鸿蒙系统后续的大规模推广也提前做好了技术储备。</p><p>当然，故事到这里并没有结束。在最基本的运行和交互能力之上，我们更需要关注 Flutter 与鸿蒙自身生态的结合：如何优雅地适配鸿蒙的分布式技术？如何用 Flutter 实现设备之间的快速连接、资源共享？现有的众多 Flutter 插件如何应用到鸿蒙系统上？未来 MTFlutter 团队将在这些方面做更深入的探索，因为解决好这些问题，才是真正能让应用覆盖用户生活的全场景的关键。</p><h2 id="参考文献">参考文献</h2><ul><li><a href="https://developer.huawei.com/consumer/cn/events/hdc2020/">https://developer.huawei.com/consumer/cn/events/hdc2020/</a></li><li><a href="https://developer.harmonyos.com/cn/documentation">https://developer.harmonyos.com/cn/documentation</a></li><li><a href="https://flutter.dev/docs/resources/architectural-overview">https://flutter.dev/docs/resources/architectural-overview</a></li><li><a href="https://github.com/flutter/flutter/wiki/Custom-Flutter-Engine-Embedders">https://github.com/flutter/flutter/wiki/Custom-Flutter-Engine-Embedders</a></li></ul><h2 id="作者简介">作者简介</h2><p>杨超，2016 年加入美团外卖技术团队，目前主要负责 MTFlutter 相关的基础建设工作。</p>  
</div>
            