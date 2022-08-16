
---
title: 'Android 13 正式发布，提供预测返回手势、生产力改进...'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fb7bbb103faec9f729c18d1d84dddb64ec0.png'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 00:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fb7bbb103faec9f729c18d1d84dddb64ec0.png'
---

<div>   
<div class="content">
                                                                                            <p>谷歌开发团队已将 Android 13 源代码推送到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsource.android.com%2F" target="_blank">Android 开源项目</a>(AOSP) ，并正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F08%2Fandroid-13-is-in-aosp.html" target="_blank">发布</a>最新版本的 Android 13。</p> 
<p>对于开发者，Android 13 专注于隐私和安全以及开发者生产力。此外，Android 13 还致力于成为更好的平板电脑和大屏幕操作系统。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>开发人员生产力和工具</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">主题应用图标</strong></li> 
</ul> 
<p>Android 13 将 Material You 动态颜色扩展到所有应用图标，用户可以选择继承其壁纸色调和其他主题偏好的图标。因此，开发应用程序的时候只需提供一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Fpractices%2Fui_guidelines%2Ficon_design_adaptive%23design-adaptive-icons" target="_blank">单色应用程序图标</a>，和对自适应图标 XML 的调整。</p> 
<p><img alt height="490" src="https://oscimg.oschina.net/oscnet/up-fb7bbb103faec9f729c18d1d84dddb64ec0.png" width="500" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">改进的日文文本换行</strong> <strong style="color:rgba(0, 0, 0, 0.67)">-</strong> TextViews 现在可以通过文集（听起来自然的最小单词单位）或短语（而不是字符）来换行文本，以获得更优美和可读的日文应用程序。下图是启用短语样式（底部文字）和未启用（顶部文字）的日语文本换行：</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="483" src="https://static.oschina.net/uploads/space/2022/0318/074203_GTyE_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>改进了非拉丁脚本（non-latin scripts）的行高 -</strong><span> </span>Android 13 通过使用适合每种语言的行高来改进非拉丁脚本（例如泰米尔语、缅甸语、泰卢固语和藏语）的显示，新的行高可防止剪裁并改善字符的定位。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="317" src="https://static.oschina.net/uploads/space/2022/0318/074528_tYeW_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">颜色矢量字体</strong> <strong style="color:rgba(0, 0, 0, 0.67)">- Android 13 增加了对 COLR 版本 1（</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Ftypography%2Fopentype%2Fspec%2Fcolr" target="_blank">规范</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DBmqYm5Wwz8M" target="_blank">介绍视频</a>）字体的渲染支持，并将系统表情符号更新为 COLRv1 格式。COLRv1 是一种新的、高度紧凑的字体格式，可以在任何大小下快速清晰地呈现。</li> 
</ul> 
<p><img alt="△ COLRv1 矢量表情符号 (左) 和位图表情符号" src="https://devrel.andfun.cn/devrel/posts/2022/03/XepxOt.png" referrerpolicy="no-referrer"></p> 
<p><em>COLRv1 矢量表情符号（左）和位图表情符号。</em></p> 
<ul> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">Quick Settings Placement API</strong></li> 
</ul> 
<p>对于提供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fservice%2Fquicksettings%2FTileService" target="_blank">自定义 Quick Settings 磁贴</a>的应用，Android 13 让用户更容易发现和添加磁贴。</p> 
<p>使用新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fapp%2FStatusBarManager%23requestAddTileService%28android.content.ComponentName%2C%2520java.lang.CharSequence%2C%2520android.graphics.drawable.Icon%2C%2520java.util.concurrent.Executor%2C%2520java.util.function.Consumer%253Cjava.lang.Integer%253E%29" target="_blank">磁贴放置 API</a>，应用可以提示用户在一个步骤中直接添加自定义快速设置磁贴，而无需离开您应用。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F13%2Ffeatures%23quick-settings" target="_blank">更多详情在这里</a>。</p> 
<ul> 
 <li style="text-align:left"><strong style="color:rgba(0, 0, 0, 0.67)">可编程着色器</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Android 13 引入了可编程 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fgraphics%2FRuntimeShader" target="_blank">RuntimeShader</a> 对象，其行为使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Ftopics%2Fgraphics%2Fagsl" target="_blank">Android 图形着色语言 (AGSL)</a> 定义。可以使用这些着色器在您的应用程序中创建<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcs.android.com%2Fandroid%2Fplatform%2Fsuperproject%2F%2B%2Fmaster%3Aframeworks%2Fbase%2Fgraphics%2Fjava%2Fandroid%2Fgraphics%2Fdrawable%2FRippleShader.java%3Bl%3D24%3Fq%3DRippleShader%26sq%3D" target="_blank">波纹</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcs.android.com%2Fandroid%2Fplatform%2Fsuperproject%2F%2B%2Fmaster%3Aframeworks%2Fnative%2Flibs%2Frenderengine%2Fskia%2Ffilters%2FBlurFilter.cpp%3Fq%3DRuntimeShader%26ss%3Dandroid%252Fplatform%252Fsuperproject%26start%3D21" target="_blank">模糊</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcs.android.com%2Fandroid%2Fplatform%2Fsuperproject%2F%2B%2Fmaster%3Aframeworks%2Fbase%2Ftests%2FHwAccelerationTest%2Fsrc%2Fcom%2Fandroid%2Ftest%2Fhwui%2FStretchShaderActivity.java%3Fq%3DRuntimeShader%26ss%3Dandroid%252Fplatform%252Fsuperproject%26start%3D11" target="_blank">拉伸</a>和其他类似的高级效果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Ftopics%2Fgraphics%2Fagsl" target="_blank">更多详情在这</a></p> 
<ul> 
 <li style="text-align:left"><strong style="color:rgba(0, 0, 0, 0.67)">PlaybackState 派生的媒体控件</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Android 13 系统从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fmedia%2Fsession%2FPlaybackState" target="_blank">PlaybackState</a> 派生了媒体控件，提供更丰富的多媒体控件集，这些控件在手机和平​​板设备之间保持一致，并与其他 Android 平台（如 Android Auto 和 Android TV）保持一致。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="369" src="https://oscimg.oschina.net/oscnet/up-56cc921cb9232f040fb5026a69e2f46989d.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F13%2Fbehavior-changes-13%23playback-controls" target="_blank">更多详情在这里</a></p> 
<ul> 
 <li style="text-align:left"><strong style="color:rgba(0, 0, 0, 0.67)">蓝牙 LE 音频 </strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bluetooth.com%2Flearn-about-bluetooth%2Frecent-enhancements%2Fle-audio%2Fresources%2F" target="_blank">低功耗 (LE) 音频</a>是下一代无线音频，支持新的用例，例如向朋友共享和广播音频，或订阅公共广播以获得信息、娱乐。它确保用户可以在不牺牲电池寿命的情况下接收高保真音频，并在不同的用例之间无缝切换。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Android 13 增加了对 LE Audio 的内置支持，因此开发人员可以在兼容设备上使用新功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fbluetooth%2FBluetoothLeAudio" target="_blank">更多详情在这里</a>。</p> 
<ul> 
 <li style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>MIDI 2.0 支持</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Android 13 增加了对新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.midi.org%2Fmidi-articles%2Fdetails-about-midi-2-0-midi-ci-profiles-and-property-exchange" target="_blank">MIDI 2.0 标准</a>的支持，包括通过 USB 连接 MIDI 2.0 硬件的能力。这提供了像提高控制器分辨率、更好地支持非西方语调，以及使用每个音符控制器的表现力等功能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fmedia%2Fmidi%2FMidiDeviceInfo%23PROTOCOL_UMP_MIDI_2_0" target="_blank">更多详情在这里</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>OpenJDK 11 更新</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Android 13 核心库现在与 OpenJDK 11 LTS 版本保持一致，为应用程序和平台开发人员提供库更新和 Java 11 编程语言支持。目前计划通过 Google Play 系统更新将这些核心库更改引入更多设备，作为运行 Android 12 及更高版本设备的 ART 模块更新的一部分。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F13%2Ffeatures%23core-libraries" target="_blank">更多详情在这里</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>预测返回手势</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Android 13 引入了新的 API，可让应用通知系统提前处理返回事件，这种做法被称为“提前”模型。这种新方法是多年努力的一部分，可以使应用程序支持预测性后退手势，该手势可通过开发者选项在 Android 13 中进行测试。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Fnavigation%2Fpredictive-back-gesture" target="_blank">更多详情在这里</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start"><span><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为平板电脑打造</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Android 13 扩展了今年早些时候发布的 12L 更新，在平板电脑上提供了更好的体验。比如增强的多任务任务栏、系统 UI 和应用程序中的更多大屏幕布局和优化、改进的应用程序兼容性模式等功能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span style="color:rgba(0, 0, 0, 0.67)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="387" src="https://oscimg.oschina.net/oscnet/up-14a9065e357461e920459f61e9ce7067a7d.gif" width="600" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><br> </p> 
<p> </p>
                                        </div>
                                      
</div>
            