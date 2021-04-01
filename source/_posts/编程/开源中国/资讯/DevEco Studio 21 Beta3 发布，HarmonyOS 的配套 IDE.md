
---
title: 'DevEco Studio 2.1 Beta3 发布，HarmonyOS 的配套 IDE'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0401/072754_04rq_2720166.gif'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 07:38:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0401/072754_04rq_2720166.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>2021年3月，DevEco Studio 迎来更新，2.1 Beta3 版本发布。</p> 
<p>HUAWEI DevEco Studio（以下简称 DevEco Studio）是面向华为终端全场景多设备的一站式集成开发环境 (IDE)，为开发者提供工程模板创建、开发、编译、调试、测试、发布等 E2E 的 HarmonyOS 应用开发服务。通过使用 DevEco Studio，开发者可以更高效地开发具备 HarmonyOS 分布式能力的应用，进而提升创新效率。</p> 
<p>下面看看此版本的更新亮点。</p> 
<h1>一、预览器新增双向预览功能</h1> 
<p>在 HarmonyOS 应用开发过程中，开发者可通过点击“Previewer”查看应用的 UI 界面效果。当开发者发现 UI 界面的布局显示不符合预期时（eg:控件的宽度不符合设定值、控件不显示等），需要逐一排查 UI 界面中布局或控件的异常。</p> 
<p><strong>为了提高排查的效率，DevEco Studio 2.1 Beta3 在已有的“实时预览”和“动态预览”基础上，全新解锁了双向预览功能。</strong></p> 
<ul> 
 <li><strong>实时预览：</strong>只要在布局文件中保存了修改的源代码，在预览器中就可以实时查看布局效果。</li> 
 <li><strong>动态预览：</strong>在预览器界面，可以在预览器中操作应用的交互动作，如点击事件、跳转、滑动等，与应用运行在真机设备上的交互体验一致。</li> 
</ul> 
<p>所谓双向预览，即支持代码编辑器、预览器界面（含属性列表）两者之间的联动，便于快速定位控件，从而提升解决 UI 界面问题的效率。开发者可以通过在预览器界面，点击图片图标的方式，打开双向预览功能。</p> 
<p>具体联动效果如下：</p> 
<p>①通过预览器界面中的属性列表，修改属性或样式后，代码编辑器中的源码会同步修改，并实时刷新预览器界面；</p> 
<p>②同样的，如果在代码编辑器中修改源码，将会实时刷新预览器界面及属性列表。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0401/072754_04rq_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>但值得注意的是，若碰到以下情况，则不支持修改其属性：</p> 
<ul> 
 <li> <p>HTML 布局代码里使用了数据绑定的属性；</p> </li> 
 <li> <p>XML 布局代码里使用了资源引用的属性；</p> </li> 
 <li> <p>UI 界面设置了动画效果。</p> </li> 
</ul> 
<p>温馨提示：不同的 API Version 版本，预览器支持的功能略有不同，具体差异如下：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0401/072705_wfpI_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>二、预览器新增Java UI界面的数据模拟功能</h1> 
<p>在预览场景中，由于代码的运行环境与真机设备上的运行环境不同，调用部分接口时无法获取到有效的返回值。开发者若想根据返回值做出不同的 UI 界面展现，则需手动反复修改代码逻辑，以验证不同 UI 界面效果。</p> 
<p><strong>为了减少修改，DevEco Studio 提供 PreviewMock 数据模拟功能，即在不改变业务运行逻辑的前提下，模拟 API 或者业务代码中的各种 method（不包括构造方法）的返回值和对象中的 Field（不包括 final 字段）的值。</strong>这样开发者就可以在预览时，查看到不同返回值带来的界面变化。</p> 
<p>不过值得注意的是，DevEco Studio 2.1 Beta3 当前仅支持 Java UI 界面的 PreviewMock 数据模拟功能。与此同时，要想使用 PreviewMock 数据模拟功能，需先在模块的 build.gradle 中添加相关依赖，并重新同步工程。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0401/072922_5brm_2720166.png" referrerpolicy="no-referrer"></p> 
<p>（图：在 build.gradle 中添加 PreviewMock 的依赖）</p> 
<p>除了上述的两大亮点功能，在 Java UI 界面预览方面，开发者在预览 Ability 或 AbilitySlice 时，保存修改后的代码，即可做到实时预览；在 JS UI 界面预览方面，开发者可直接选择某一个 page（页面）进行实时动态预览。</p> 
<h1>三、编辑器新增 config.json 可视化配置功能</h1> 
<p>作为 HarmonyOS 应用开发的入门选手，你是否为了了解配置项的含义，而反复查阅 HarmonyOS 官网的资料文档？<strong>为了减少开发者反复切换界面查阅资料文档的行为，DevEco Studio 2.1 Beta3 新增了可视化配置功能。</strong></p> 
<p>开发者可通过打开 config.json 文件，点击<img src="https://static.oschina.net/uploads/space/2021/0401/073102_I8E2_2720166.png" referrerpolicy="no-referrer">按钮，打开设置界面，查看该项目所需填写的重要属性及其含义，完善应用名称、应用版本号、应用类型、Ability、设备类型、应用权限等配置项。</p> 
<p>然而，在开发过程中，可能存在配置项层级过多的场景，例如：配置“Module › Ablilities › Meta Data › Merge Rule › Replace”字段时，用户可通过搜索框快速定位到该属性，点击 add 按钮，输入相关合并规则，触发系统在 config.json 文件中自动创建配置项的树型结构，完成合并规则的配置，节省配置时间。</p> 
<h1>四、编辑器新增资源创建向导功能</h1> 
<p>开发者在创建带限定词的资源目录时，需考虑限定词的取值、不同限定词相互搭配时的先后顺序等，稍有偏差则会导致应用在运行时，HarmonyOS 检测不到合适的资源，无法呈现预期效果。</p> 
<p><strong>为了降低开发者在创建带限定词的资源目录时的出错机率，DevEco Studio 2.1 Beta3 新增了资源创建向导功能，用户根据界面提示进行选择或输入，即可完成资源目录及文件的创建，无需思索各种限定词之间的组合关系。</strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0401/073729_Fxwn_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>除了上述的亮点功能，DevEco Studio 2.1 Beta3 在编辑器方面，还做了其它优化，具体优化细节如下：</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0401/073246_z3Eb_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>五、新增 Java 测试框架</h1> 
<p><strong>为了减化繁琐的人工测试环节，DevEco Studio 2.1 Beta3 新增了 Java 测试框架，提供 Java 代码白盒测试能力，帮助开发者高效编写和执行测试用例，保障应用基础质量。</strong></p> 
<p>在开发阶段，开发者可借助由 Java 测试框架提供的 IAbilityDelegator，进行 APP 组件操控测试（如：启动/关闭 FA、获取界面 UI 元素、注入 UI 点击事件等），及时发现 UI 交互问题。或使用 JUnit 4 语法范式，编写测试用例、调用系统接口，获得 API 返回值或触发业务流程，根据接口返回值或业务状态，判断业务逻辑的正确性。</p> 
<p><strong>Java </strong><strong>测试框架在真机或远程模拟器设备上运行的前提：</strong></p> 
<p>① 远程模拟器需注册开发者账号并完成实名认证；</p> 
<p>② 真机设备需搭载 HarmonyOS 操作系统，并打开调试模式，且有相应的签名文件。</p> 
<h1>六、新增 5 个手机 (Phone) 工程模板</h1> 
<p>DevEco Studio 支持手机(Phone)、平板(Tablet)、车机(Car)、智慧屏(TV)、智能穿戴(Wearable)、轻量级智能穿戴(Lite Wearable)和智慧视觉(Smart Vision)七种设备的 HarmonyOS 应用开发，支持 Java、JS 和 C/C++ 编程语言。</p> 
<p>为了方便开发者的使用，DevEco Studio 提供了多设备类型、不同开发语言的 Ability 模板。<strong>本次的新版本，在原有的基础上，新增了 5 个手机(Phone)工程模板，目前手机(Phone)工程模板共 19 个。</strong>开发者们可根据工程向导，挑选合适的模板，轻松创建适用于各类设备的工程，并自动生成对应的代码和资源模板。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0401/073519_lB0P_2720166.png" referrerpolicy="no-referrer"></p> 
<p>除了以上的六大亮点，DevEco Studio 2.1 Beta3 在开发者打开历史工程时，会提示开发者将历史工程进行升级适配，点击提示中的“<strong>Update</strong>”，即可一键自动化修改工程中的配置信息，省去开发者逐一修改相关配置的烦恼。</p> 
<p><strong>除此之外，DevEco Studio 2.1 Beta3 还在不少细节上进行了优化。下面请看细节清单：</strong></p> 
<p>①升级 IntelliJ IDEA 底座至 IntelliJ IDEA CommunityEdition 2020.2.4 版本（温馨提示：由于底座升级，开发者需要手工升级不可用的三方插件，避免出现已安装的三方插件不兼容情况）</p> 
<p>②在调试阶段，开发者可设置 hap 包的安装方式。若选择覆盖安装，则会保留已安装应用内的缓存数据，无需重装应用后再重新构建相关数据，方便调试。</p> 
<p>③解决了部分开发者下载 Node.js 缓慢或者失败的问题。通过集成 Node.js 并预置华为公有云的 npm 仓，进一步缩短搭建 HarmonyOS 应用开发环境的时间。</p> 
<p>④已适配支持 macOS11.2.2 版本。</p> 
<p>⑤解决了 XML 里面的 drawable 的资源无法联想的问题。</p> 
<p>获取新版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdevelop%2Fdeveco-studio%23download" target="_blank">https://developer.harmonyos.com/cn/develop/deveco-studio#download</a></p>
                                        </div>
                                      
</div>
            