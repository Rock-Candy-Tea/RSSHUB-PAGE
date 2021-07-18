
---
title: '优化移动游戏性能 _ 来自Unity顶级工程师的性能分析、内存与代码架构小贴士'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202107/08/142907z0gtvluclw4tgvwc.jpg'
author: GameRes 游资网
comments: false
date: Thu, 08 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/08/142907z0gtvluclw4tgvwc.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2503710">
Unity Accelerate Solution 团队对 Unity 引擎的源代码了如指掌，可帮助客户们最大限度地利用引擎。团队的日常工作包括深入剖析客户项目，搜寻其在速度、稳定性与效率方面有待优化的部分。本次，我们请到了这支 Unity 最为资深的软件工程师团队来分享一些移动游戏优化方面的专业知识。<br>
<br>
他们分享了非常多的锦囊妙计，以至于一篇博文很难涵盖所有内容。因此，我们将推出一个博文系列。作为此系列的首篇文章，我们将着重介绍怎样借助性能分析、内存优化和代码架构来提高游戏的性能。在未来的几周内，我们将再发表两篇文章：一篇讨论 UI Physics，另一篇讨论音频和资源、项目配置和图形。<br>
<br>
话不多说，直接开讲！<br>
<br>
<strong><font color="#de5650">性能分析</font></strong><br>
<br>
优化工作的第一个步骤便是通过性能分析来收集性能数据，这也是移动端优化的第一步。<br>
我们要尽早在目标设备上进行性能分析，而且要经常分析。<br>
<br>
Unity Profiler 可提供应用关键的性能信息，因此是优化必不可少的一部分。尽早对项目进行性能分析，不要拖到发售前。对每一个故障或性能尖峰彻查到底。对你自己的项目性能有一个清晰的认知，可帮助你更轻松地发现新问题。<br>
<br>
Unity 编辑器内的性能分析可以揭示出游戏不同系统的相对性能，而在运行设备上进行分析可让你获取更为准确的性能洞察。经常性地在目标设备上分析开发版。同时为最高配置与最低配置的设备进行性能分析和优化。<br>
<br>
除了 Unity Profiler，你还可以使用 iOS 与 Android 的原生工具来进一步测试引擎在平台上的表现。<br>
<br>
<ul><li>比如 iOS 的 Xcode 和 Instruments</li><li>以及 Android 上的 Android Studio 和 Android Profiler<br>
</li></ul><br>
部分硬件更是带有额外的分析工具（例如 Arm Mobile Studio、Intel VTune 以及 Snapdragon Profiler）。<br>
<br>
Unity Profiler：<br>
<br>
https://docs.unity3d.com/Manual/Profiler.html<br>
<br>
Xcode：<br>
<br>
https://developer.apple.com/documentation/xcode/<br>
<br>
Instruments：<br>
<br>
https://help.apple.com/instruments/mac/current/#/dev7b09c84f5<br>
<br>
Android Studio：<br>
<br>
https://developer.android.com/studio/intro<br>
<br>
Android Profiler：<br>
<br>
https://developer.android.com/studio/profile/android-profiler<br>
<br>
Arm Mobile Studio：<br>
<br>
https://developer.arm.com/tools-and-software/graphics-and-gaming/arm-mobile-studio<br>
<br>
Intel VTune：<br>
<br>
https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top.html<br>
<br>
Snapdragon Profiler：<br>
<br>
https://developer.qualcomm.com/software/snapdragon-profiler<br>
<br>
<strong><font color="#de5650">针对性优化</font></strong><br>
<br>
如果游戏出现性能问题，切忌自行猜测或揣测成因，一定要使用 Unity Profiler 和平台专属工具来准确找出卡顿的问题来源。<br>
<br>
不过，这里所说的优化并不都适用于你的应用。在某个项目中适用的方法不一定适用于你的项目。找出真正的性能瓶颈，将精力集中在有实际效用的地方。<br>
<br>
<strong><font color="#de5650">了解 Unity Profiler 工作原理</font></strong><br>
<br>
Unity Profiler 可帮助你在运行时检测出卡顿或死机的原因，更好地了解特定帧或时间点上发生了什么。工具默认启用 CPU 和内存监测轨，你也可以根据需要启用额外的分析模块，包括渲染器、音频和物理（如极度依赖物理模拟的游戏或音游）。<br>
<br>
<div align="center">
<img id="aimg_991179" aid="991179" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142907z0gtvluclw4tgvwc.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142907z0gtvluclw4tgvwc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142907z0gtvluclw4tgvwc.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">或使用Unity Profiler来测试应用程序的性能和资源分配</font></font></div><br>
勾选 Development Build 便能为目标设备构建应用，勾选 Autoconnect Profiler 或者手动关联分析器，来加快其启动时间。<br>
<br>
<div align="center">
<img id="aimg_991180" aid="991180" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142908f6ueleqsr6qq2so6.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142908f6ueleqsr6qq2so6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142908f6ueleqsr6qq2so6.jpg" referrerpolicy="no-referrer">
</div><br>
选中需要分析的目标平台。按下 Record（录制）按钮可记录应用在几秒钟内的运行（默认为300帧）。打开 Unity > Preferences > Analysis > Profiler > Frame Count 界面可修改录制帧数，最长录制帧数可以增加到 2000帧。当然更长的录制帧数会让 Unity 编辑器占用更多的 CPU 资源和内存，但其在特定情形下的作用非常大。<br>
<br>
该分析器采用标记框架，可分析以 ProfileMarkers（如MonoBehaviour的Start或Update方法，或特定API调用）划分出的代码运行时。在使用 Deep Profiling 时，Unity 可以分析出每次函数调用的开始与结尾，准确地呈现出导致应用性能放缓的代码部分。<br>
<br>
ProfileMarkers：<br>
<br>
https://docs.unity.cn/ScriptReference/Unity.Profiling.ProfilerMarker.html<br>
<br>
Deep Profiling：<br>
<br>
https://docs.unity.cn/cn/current/Manual/ProfilerWindow.html<br>
<br>
<div align="center">
<img id="aimg_991181" aid="991181" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142909rj43op0j0fxz8h3p.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142909rj43op0j0fxz8h3p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142909rj43op0j0fxz8h3p.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">你可以借助Timeline视图来明确应用最为依赖的是CPU还是GPU</font></font></div><br>
在分析游戏时，我们建议同时分析性能高峰与帧平均成本。在分析帧率过低的应用时，较为有效的方法是分析并优化每一帧中运行成本较高的代码。在尖峰处首先分析繁重的运算（如物理、AI、动画）和垃圾数据收集。<br>
<br>
点击窗口中的某帧，接着使用 Timeline 或 Hierarchy 视图进行分析：<br>
<br>
<ul><li>图片 Timeline 可显示特定帧耗时的可视化图表，帮助你直观地看到各项活动以及不同线程之间的关系。你可使用该选项来了解项目主要依赖的是 CPU 还是 GPU。</li><li>Hierarchy 将显示分组的 ProfileMarkers 层级，并以毫秒（Time ms'总耗时'和Self ms‘自执行耗时’）为单位对样本进行排序。你还可以数出帧上函数的 Calls 调用以及内存清理（GC Alloc）的次数。<br>
</li></ul><br>
<div align="center">
<img id="aimg_991182" aid="991182" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142910h3j5jhhox5jzhiyf.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142910h3j5jhhox5jzhiyf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142910h3j5jhhox5jzhiyf.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Hierarchy视图允许按照耗时长短对ProfileMarkers进行排序</font></font></div><br>
注意，在优化任意项目之前，一定要保存 Profiler 的 .data 文件，这样你就能在修改后比较优化前后的不同了。剖析、优化和比较，清空再重复，如此循环往复来提高性能。<br>
<br>
<strong><font color="#de5650">Profiler Analyzer</font></strong><br>
<br>
该工具可以汇总多帧 Profiler 数据，由用户来挑选出那些问题较大的帧。如果你想了解项目更改后 Profiler 的相应改变，可使用 Compare 视图分别加载和比较两个数据集，从而完成测试与优化。Profile Analyzer 可在 Unity Package Manager 中下载。<br>
<br>
Profile Analyzer：<br>
<br>
https://docs.unity3d.com/Packages/com.unity.performance.profile-analyzer@1.0/manual/index.html<br>
<br>
<div align="center">
<img id="aimg_991183" aid="991183" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142912vijyun2e6imnujtu.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142912vijyun2e6imnujtu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142912vijyun2e6imnujtu.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Profiler Analyzer可以很好地补充Profiler，可以进一步深入分析帧与标记数据</font></font></div><br>
<strong><font color="#de5650">为每帧设定一个时间预算</font></strong><br>
<br>
你可以设立一个目标帧率，为每帧划定一个时间预算。理想情况下，一个以 30 fps 运行的应用每帧应占有约 33.33 毫秒（1000毫秒/30帧）。同样地，60 fps 每帧约为 16.66 毫秒。<br>
<br>
设备可以在短时间内超过预算（如过场动画或加载过程中），但绝不能长时间如此。<br>
<br>
<strong><font color="#de5650">设备温度优化</font></strong><br>
<br>
对于移动设备而言，长时间占用最大时间预算可能会导致设备过热，操作系统可能会启动 CPU 与 GPU 降频保护。我们建议每帧仅占用约 65% 的时间预算，保留一定的散热时间。常见的帧预算为：30 fps 为每帧 22 毫秒，60 fps 为每帧 11 毫秒。<br>
<br>
大多数移动设备不像桌面设备那样有主动散热功能，因此环境温度可以直接影响性能。<br>
<br>
如果设备发热严重，Profiler 可能会察觉并汇报这块性能低下的部分，即使其只是暂时性问题。为了应对分析时设备过热，分析应分成小段进行。这样便能允许设备散热、模拟出真实的运行条件。我们的建议是，在进行性能分析前后，预留 10-15 分钟用于设备散热。<br>
<br>
<strong><font color="#de5650">分清 GPU 与 CPU 依赖程度</font></strong><br>
<br>
Profiler 可在 CPU 耗时或 GPU 耗时超出帧预算发出警告，它将弹出下方以 Gfx 为前缀的标记：<br>
<br>
<ul><li>Gfx.WaitForCommands 标记表示渲染线程正在等待主线程完成，后者可能出现了性能瓶颈。</li><li>而 Gfx.WaitForPresent 表示主线程正在等待 GPU 递交渲染帧。<br>
</li></ul><br>
<strong><font color="#de5650">内存分析</font></strong><br>
<br>
Unity 会采取自动化内存管理来处理由用户生成的代码与脚本。值类型本地变量等小型数据会被分配到内存堆栈中，大型数据和持久性存储数据则会被分配到托管内存中。<br>
<br>
垃圾数据收集器会定期识别并删除未被使用的托管内存，这个自动流程在检查堆的对象时可能导致游戏卡顿或运行放缓。<br>
<br>
这里，优化内存便是指关注托管内存的分配与删除时机，将内存垃圾回收的影响降到最低。详情请在 Understanding the managed heap 中了解。<br>
<br>
Understanding the managed heap：<br>
<br>
https://docs.unity.cn/cn/current/Manual/BestPracticeUnderstandingPerformanceInUnity4-1.html<br>
<br>
<div align="center">
<img id="aimg_991184" aid="991184" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142913izxnfyhyp0545xzp.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142913izxnfyhyp0545xzp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142913izxnfyhyp0545xzp.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Memory Profiler中的帧数据记录、检视与比较</font></font></div><br>
<strong><font color="#de5650">Memory Profiler</font></strong><br>
<br>
Memory Profiler 属于一个独立的分析模块，可以截取托管数据堆内存的状态，帮助你识别出数据碎片化和内存泄漏等问题。<br>
<br>
在 Tree Map 视图中点击一个变量便可跟踪其在内存原生对象上的状态。你可在此处找出由纹理过大或资源重复加载而导致的常见内存消耗问题。<br>
<br>
通过以下链接了解如何使用 Unity 的 Memory Profiler 优化内存占用。<br>
<br>
Memory Profiler：<br>
<br>
https://docs.unity3d.com/Packages/com.unity.memoryprofiler@0.2/manual/index.html<br>
<br>
<strong><font color="#de5650">降低内存垃圾回收（GC）对性能的影响</font></strong><br>
<br>
Unity 使用的是 Boehm-Demers-Weiser 垃圾回收器 ，它会中止主线程代码运行，在垃圾回收工作完成后再让其恢复运行。<br>
<br>
请注意，部分多余的托管内存分配会造成 GC 耗能高峰：<br>
<br>
<ul><li>Strings（字符串）：在 C# 中，字符串属于引用类型，而非值类型。我们需要减少不必要的字符串创建或更改操作，尽量避免解析 JSON 和 XML 等由字符串组成的数据文件，将数据存储于 ScriptableObjects，或以 MessagePack 或 Protobuf 等格式保存。如果你需要在运行时构建字符串，可使用 StringBuilder 类。</li><li>Unity 函数调用：部分函数会涉及托管内存分配。我们需要缓存数组引用，避免在循环进行中进行数组的内存分配，且尽量使用那些不会产生垃圾回收的函数。比如使用 GameObject.CompareTag，而不是使用 GameObject.tag 手动比对字符串（因为返回一个新字符串会产生垃圾数据）。</li><li>Boxing（打包）：避免在引用类型变量处传入值类型变量，因为这样做会导致系统创建一个临时对象，在背地里将值类型转换为对象类型（如int i = 123; object o = i ），从而产生垃圾回收的需求。尽量使用正确的类型覆写来传入想要的值类型。泛型也可用于类型覆写。</li><li>Coroutines（协同程序）：虽然 yield 不会产生垃圾回收，但新建 WaitForSeconds 对象会。我们可以缓存并复用 WaitForSeconds 对象，不必在 yield 中再度创建。</li><li>LINQ 与 Regular Expressions（正则表达式）：这两种方法都会在后台的数据打包期间产生垃圾回收。如果需要追求性能，请尽量避免使用 LINQ 和正则表达式，转而使用 for 循环和列表来创建数组。<br>
</li></ul><br>
Boehm-Demers-Weiser 垃圾回收器：<br>
<br>
https://www.hboehm.info/gc/<br>
<br>
<strong><font color="#de5650">定时处理垃圾回收</font></strong><br>
<br>
如果你确定垃圾回收带来的卡顿不会影响游戏特定阶段的体验，你可以使用 System.GC.Collect 来启动垃圾数据收集。<br>
<br>
请在 Understanding Automatic Memory Management（自动化内存管理）中了解怎样妥善地使用这项功能。<br>
<br>
Understanding Automatic Memory Management：<br>
<br>
https://docs.unity.cn/cn/current/Manual/UnderstandingAutomaticMemoryManagement.html<br>
<br>
<strong><font color="#de5650">使用增量式垃圾回收（Incremental GC）分散垃圾回收</font></strong><br>
<br>
增量式垃圾回收不会在程序运行期间长时间地中断运行，而会将总负荷分散到多帧，形成零碎的收集流程。如果垃圾数据收集对性能产生了较大的影响，可以尝试启用这个选项来降低 GC 的处理高峰。你可以使用 Profile Analyzer 来检验此功能的实际作用。<br>
<br>
<div align="center">
<img id="aimg_991185" aid="991185" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142913cp7aeejq17d3r3ru.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142913cp7aeejq17d3r3ru.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142913cp7aeejq17d3r3ru.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">使用增量垃圾回收来降低GC处理高峰</font></font></div><br>
<strong><font color="#de5650">编程和代码架构</font></strong><br>
<br>
Unity 的 PlayerLoop 包含许多可与引擎核心互动的函数。该结构包含一些负责初始化和每帧更新的系统，所有脚本都将依靠 PlayerLoop 来生成游戏体验。<br>
<br>
在分析时，你会在 PlayerLoop 下看到用户使用的代码（Editor代码则位于EditorLoop下）。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_991186" aid="991186" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142914t2ttp3ywewl260vy.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142914t2ttp3ywewl260vy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142914t2ttp3ywewl260vy.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Profiler将显示在整个引擎运行过程中的自定义脚本、设置和图形</font></font></div><br>
<div align="center">
<img id="aimg_991187" aid="991187" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142914zsttdbfnmat6ds6b.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142914zsttdbfnmat6ds6b.jpg" width="577" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142914zsttdbfnmat6ds6b.jpg" referrerpolicy="no-referrer">
</div><br>
通过以下链接了解 PlayerLoop 和 脚本生命周期 。<br>
<br>
PlayerLoop：<br>
<br>
https://docs.unity.cn/ScriptReference/LowLevel.PlayerLoop.html<br>
<br>
脚本生命周期：<br>
<br>
https://docs.unity.cn/cn/2020.3/Manual/ExecutionOrder.html<br>
<br>
你可以使用以下技巧和窍门来优化脚本。<br>
<br>
<strong><font color="#de5650">深入理解 Unity PlayerLoop</font></strong><br>
<br>
我们需要掌握 Unity 帧循环的执行顺序 。每个 Unity 脚本都会按照预定的顺序运行事件函数，这要求我们了解 Awake、Start、Update 以及其他运行周期相关函数之间的区别。<br>
<br>
请在 Script Lifecycle Flowchart（脚本生命周期流程图）中了解函数的执行顺序。<br>
<br>
Script Lifecycle Flowchart：<br>
<br>
https://docs.unity.cn/cn/2020.3/Manual/ExecutionOrder.html<br>
<br>
<strong><font color="#de5650">降低每帧的代码量</font></strong><br>
<br>
有许多代码并非要在每帧上运行，这些不必要的逻辑完全可以在 Update、LateUpdate 和 FixedUpdate 中删去。这些事件函数可以保存那些必须每帧更新的代码，任何无须每帧更新的逻辑都不必放入其中，只有在相关事物发生变化时，这些逻辑才需被执行。<br>
<br>
如果必须要使用 Update，可以考虑让代码每隔 n 帧运行一次。这种划分运行时间的方法也是一种将繁重工作负荷化整为零的常见技术。在下方例子中，ExampleExpensiveFunction 将每隔三帧运行一次。<br>
<br>
<div class="blockcode"><div id="code_N5j"><ol><li>private int interval = 3;<br>
</li><li><br>
</li><li>void Update()<br>
</li><li>&#123;<br>
</li><li>    if (Time.frameCount % interval == 0)<br>
</li><li>    &#123;<br>
</li><li>        ExampleExpensiveFunction();<br>
</li><li>    &#125;<br>
</li><li>&#125;</li></ol></div><em onclick="copycode($('code_N5j'));">复制代码</em></div><br>
<strong><font color="#de5650">避免在 Start/Awake 中加入繁重的逻辑</font></strong><br>
<br>
当首个场景加载时，每个对象都会调用如下函数：<br>
<br>
<ul><li>Awake</li><li>OnEnable</li><li>Start<br>
</li></ul><br>
在应用完成第一帧的渲染前，我们须避免在这些函数中运行繁重的逻辑。否则，应用的加载时间会出乎意料地长。<br>
<br>
请在 Order of execution for event functions（事件函数的执行顺序）中详细了解首个场景的加载。<br>
<br>
Order of execution for event functions：<br>
<br>
https://docs.unity.cn/cn/2020.3/Manual/ExecutionOrder.html<br>
<br>
<strong><font color="#de5650">避免加入空事件</font></strong><br>
<br>
即使是空的 MonoBehaviours 也会占用资源，因此我们应该删除空的 Update 及 LateUpdate 方法。<br>
<br>
如果你想用这些方法进行测试，请使用预处理指令（preprocessor directives）：<br>
<br>
<div class="blockcode"><div id="code_d5s"><ol><li>#if UNITY_EDITOR<br>
</li><li>void Update()<br>
</li><li>&#123;<br>
</li><li>&#125;<br>
</li><li>#endif</li></ol></div><em onclick="copycode($('code_d5s'));">复制代码</em></div><br>
如此一来，在编辑器中的 Update 测试便不会对构建版本造成不良的性能影响。<br>
<br>
<strong><font color="#de5650">删去 Debug Log 语句</font></strong><br>
<br>
Log 声明（尤其是在Update、LateUpdate及FixedUpdate中）会拖慢性能，因此我们需要在构建之前禁用 Log 语句。<br>
<br>
你可以用预处理指令编写一条 Conditional 属性来轻松禁用 Debug Log。比如下方这种的自定义类：<br>
<br>
Conditional 属性：<br>
<br>
https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.conditionalattribute?view=net-5.0<br>
<br>
<div class="blockcode"><div id="code_y5q"><ol><li>public static class Logging<br>
</li><li>&#123;<br>
</li><li>    [System.Diagnostics.Conditional("ENABLE_LOG")]<br>
</li><li>    static public void Log(object message)<br>
</li><li>    &#123;<br>
</li><li>        UnityEngine.Debug.Log(message);<br>
</li><li>    &#125;<br>
</li><li>&#125;</li></ol></div><em onclick="copycode($('code_y5q'));">复制代码</em></div><br>
<div align="center">
<img id="aimg_991188" aid="991188" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142914n44o0ss234pbx0b5.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142914n44o0ss234pbx0b5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142914n44o0ss234pbx0b5.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">添加自定义预处理指令可以实现脚本的切分</font></font></div><br>
用自定义类生成 Log 信息时，你只需在 Player Settings 中禁用 ENABLE_LOG  预处理指令，所有的 Log 语句便会一下子消失。<br>
<br>
<strong><font color="#de5650">使用哈希值、避免字符串</font></strong><br>
<br>
Unity 底层代码不会使用字符串来访问 Animator、Material 和 Shader 属性。出于提高效率的考虑，所有属性名称都会被哈希转换成属性 ID，用作实际的属性名称。<br>
<br>
在 Animator、Material 或 Shader 上使用 Set 或 Get 方法时，我们便可以利用整数值而非字符串。后者还需经过一次哈希处理，并没有整数值那么直接。<br>
<br>
使用 Animator.StringToHash 来转换 Animator 属性名称，用 Shader.PropertyToID 来转换 Material 和 Shader 属性名称。<br>
<br>
Animator.StringToHash：<br>
<br>
https://docs.unity.cn/ScriptReference/Animator.StringToHash.html<br>
<br>
Shader.PropertyToID：<br>
<br>
https://docs.unity.cn/ScriptReference/Shader.PropertyToID.html<br>
<br>
<strong><font color="#de5650">选择正确的数据结构</font></strong><br>
<br>
由于数据结构每帧可能会迭代上千次，因此其结构对性能有着较大的影响。如果你不清楚数据集合该用 List、Array 还是 Dictionary 表示，可以参考 C# 的 MSDN 数据结构指南来选择正确的结构。<br>
<br>
MSDN 数据结构指南：<br>
<br>
https://docs.microsoft.com/en-us/dotnet/standard/collections/?redirectedfrom=MSDN<br>
<br>
<strong><font color="#de5650">避免在运行时添加组件</font></strong><br>
<br>
在运行时调用 AddComponent 会占用一定的运行成本，Unity 必须检查组件是否有重复或依赖项。<br>
<br>
当组件已经配置完成，Instantiating a Prefab（实例化预制件）一般来说性能更强。<br>
<br>
Instantiating a Prefab：<br>
<br>
https://docs.unity.cn/cn/current/Manual/Prefabs.html<br>
<br>
<strong><font color="#de5650">缓存 GameObjects 和组件</font></strong><br>
<br>
调用 GameObject.Find、GameObject.GetComponent 和 Camera.main（2020.2以下的版本）会产生较大的运行负担，因此这些方法不适合在 Update 中调用，而应在 Start 中调用并缓存。<br>
<br>
下方例子展示了一种低效率的 GetComponent 多次调用：<br>
<br>
<div class="blockcode"><div id="code_jlZ"><ol><li>void Update()<br>
</li><li>&#123;<br>
</li><li>    Renderer myRenderer = GetComponent<Renderer>();<br>
</li><li>    ExampleFunction(myRenderer);<br>
</li><li>&#125;</li></ol></div><em onclick="copycode($('code_jlZ'));">复制代码</em></div><br>
其实 GetComponent 的结果会被缓存，因此只需调用一次即可。缓存的结果完全可在 Update 中重复使用，不必再度调用 GetComponent。<br>
<br>
<div class="blockcode"><div id="code_p1l"><ol><li><br>
</li><li>private Renderer myRenderer;<br>
</li><li><br>
</li><li>void Start()<br>
</li><li>&#123;<br>
</li><li>    myRenderer = GetComponent<Renderer>();<br>
</li><li>&#125;<br>
</li><li><br>
</li><li>void Update()<br>
</li><li>&#123;<br>
</li><li>    ExampleFunction(myRenderer);<br>
</li><li>&#125;</li></ol></div><em onclick="copycode($('code_p1l'));">复制代码</em></div><br>
<strong><font color="#de5650">对象池（Object Pool）</font></strong><br>
<br>
Instantiate（实例化）和 Destroy（销毁）方法会产生需要垃圾回收数据、引发垃圾回收（GC）的处理高峰，且其运行较为缓慢。与其经常性地实例化和销毁 GameObjects（如射出的子弹），不如使用对象池将对象预先储存，再重复地使用和回收。<br>
<br>
对象池：<br>
<br>
https://en.wikipedia.org/wiki/Object_pool_pattern<br>
<br>
<div align="center">
<img id="aimg_991189" aid="991189" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142915e2nnz3ahknhrkjwn.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142915e2nnz3ahknhrkjwn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142915e2nnz3ahknhrkjwn.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">在这个例子中，ObjectPool创建了20个PlayerLaser实例供重复使用</font></font></div><br>
在游戏特定时间点（如显示菜单画面时）创建可复用的实例，来降低 CPU 处理高峰的影响，再用一个集合来形成“对象池”。在游戏期间，实例可在需要时启用/禁用，用完后可返回到池中，不必再进行销毁。<br>
<br>
<div align="center">
<img id="aimg_991190" aid="991190" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142916f02efgegdpse8cgb.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142916f02efgegdpse8cgb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142916f02efgegdpse8cgb.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">PlayerLaser对象池目前尚未激活，正等待玩家射击</font></font></div><br>
这一来你就可以减少托管内存分配的次数、防止产生垃圾回收的问题。<br>
<br>
<strong><font color="#de5650">使用 ScriptableObjects（可编程对象）</font></strong><br>
<br>
固定不变的值或配置信息可以存储在 ScriptableObject 中，不一定得储存于 MonoBehaviour。ScriptableObject 可由整个项目访问，一次设置便可应用于项目全局，但它并不能直接关联到 GameObject 上。<br>
<br>
我们可在 ScriptableObject 中用字段来存储值或设定，然后在 MonoBehaviours 中引用该对象。<br>
<br>
<div align="center">
<img id="aimg_991191" aid="991191" zoomfile="https://di.gameres.com/attachment/forum/202107/08/142916q9agcwddz7af91ii.jpg" data-original="https://di.gameres.com/attachment/forum/202107/08/142916q9agcwddz7af91ii.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/08/142916q9agcwddz7af91ii.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">用作“Inventory（物品栏）”的ScriptableObject可保存多个游戏对象的设定</font></font></div><br>
下方的 ScriptableObject 字段可有效防止多次 MonoBehaviour 实例化产生的数据重复。<br>
<br>
请参考 ScriptableObjects 文档了解如何使用。<br>
<br>
ScriptableObjects：<br>
<br>
https://docs.unity.cn/cn/current/Manual/class-ScriptableObject.html<br>
<br>
<font size="2"><font color="#808080">来源：Unity官方平台</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/XNxa0oeW25R_mwCgKWp11w</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            