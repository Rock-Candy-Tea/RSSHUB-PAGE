
---
title: 'PyCharm 2022.1 EAP 2 发布：改良依赖项管理、改进 Vue 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f388c31c1e4a5c583a2ed7cb2bedff763ca.png'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f388c31c1e4a5c583a2ed7cb2bedff763ca.png'
---

<div>   
<div class="content">
                                                                                            <p>PyCharm 2022.1 EAP 2 现已推出！该版本增强 TypedDict 的代码洞察功能（对每个键进行检测）、轻松管理依赖项（在基本 Http 授权下管理自定义存储库 Python 包的能力）、对 Vue 的一些新改进，以及 Markdown 格式改进等...</p> 
<p>可从 JetBrains 官网<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fnextversion%2F" target="_blank">下载 EAP 版本</a>。<strong>重要提示：EAP 版本未经过全面测试，可能不稳定。</strong></p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-f388c31c1e4a5c583a2ed7cb2bedff763ca.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>在 macOS 上自动安装 Python</h2> 
<p style="margin-left:0px">PyCharm 现在可以为用户安装 Python 3，通常情况下 macOS 仅提供开箱即用的 Python 2.x 版本，如果你的设备上没有 Python 3，PyCharm 可以在配置系统解释器或虚拟环境时自动安装 Python 3 。</p> 
<h2>代码洞察：改进 TypedDict 键警告</h2> 
<p>每当有作为字面量创建的  <span style="background-color:#ffffff; color:#27282c">dictionary </span>或字典结构相关的函数用在需要 TypedDict 的地方（赋值、函数/方法调用、返回语句），PyCharm 会显示每个键的错误消息，准确解释哪些值有问题，以及它们出现在哪里。</p> 
<p>此外，PyCharm 现在会警告当前缺少哪些特定的字典元素，以及哪些元素未为字典定义。</p> 
<p><img alt height="333" src="https://oscimg.oschina.net/oscnet/up-f80eb8e84986ea19538a77925db0c582494.png" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="333" src="https://oscimg.oschina.net/oscnet/up-e5517a09fc45723bdac3edc199066b44aad.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>用户界面/用户体验：</h2> 
<h3>自定义 Python 包存储库</h3> 
<p>使用此 EAP 版本可以添加具有基本 HTTP 授权的自定义 Python 包存储库，并通过 PyCharm 轻松管理依赖项，而无需切换到终端进行手动安装。</p> 
<p>*新的存储库将出现在左侧窗口的包列表中。</p> 
<p><img alt height="395" src="https://oscimg.oschina.net/oscnet/up-bcc0674a45442a8ade9e2997a77209d48f5.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>新的通知工具窗口</h3> 
<p>用新的 <strong><em>通知</em> </strong>工具窗口替换了 <em><strong>事件日志实例</strong> </em>，所有通知可以分为两类：<em><strong>建议</strong></em> 和 <em><strong>时间线</strong></em>。</p> 
<p><img alt height="407" src="https://oscimg.oschina.net/oscnet/up-cc3785d88f58d45eae44cf257ae18664e31.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>Vue 支持的改进</h2> 
<p>PyCharm 2022.1 对 Vue 3 进行了多项改进：如果将组件定义为全局，IDE 现在将在 .vue 文件中识别它们，此外 PyCharm 2022.1 EAP 2 正确地支持<code>createApp</code>语法，将正确匹配使用<code>createApp</code>其相关元素创建的应用程序。</p> 
<p><img alt="vue-global-components" src="https://blog.jetbrains.com/wp-content/uploads/2022/02/vue-global-components.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start">此版本还包括对 Nuxt 3 的支持，这是 Vue 框架的一个新版本。</p> 
<h2>Markdown 格式改进</h2> 
<ul> 
 <li>从 Markdown 文件运行命令</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#27282c">README 文件一般用来描述一个软件的运行步骤，</span><span style="background-color:#ffffff; color:#27282c">PyCharm 2022.1 </span>将允许直接从这类 Markdown 文件运行命令 —— 只需单击命令左侧装订线中的<span> </span><em>运行<span> </span></em>图标即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="350" src="https://static.oschina.net/uploads/space/2022/0130/072716_8ptv_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新选项可以通过<span> </span><em>Detect 命令进行管理，这些命令可以直接从 Preferences / Settings |<span> </span></em>中的 Markdown 文件运行。</p> 
<ul> 
 <li>复制 Markdown 的代码片段</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本向 Markdown 块添加了一个新的<em>复制代码片段<span> </span></em>操作，可以快速复制 Markdown 的代码到剪贴板。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072730_2T9m_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>风险控制系统</h2> 
<h3>使用 Git Blame 更新注释</h3> 
<p style="margin-left:0; margin-right:0; text-align:start">改进了使用 <strong><em>Git Blame</em></strong> 进行注释的功能，使调查引入的更改更轻松。将鼠标悬停在注释上时，IDE 会在编辑器中突出显示不同的行，并在单击它时打开 Git Log 工具窗口。</p> 
<h3>Git 文件历史记录：没有索引的新 UI</h3> 
<p><em><strong>Git 文件历史</strong> </em>工具窗口的新 UI 现在独立于索引过程，即使 Log 索引关闭，数据也会以新界面表示。（以前，对于具有未索引历史记录的文件，IDE 会显示一个相对较慢且缺少功能的旧历史记录视图。）</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-4631be654c4c37afc4191669cc203ce72d9.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">此外，单击注释时，Git Log 工具窗口会自动打开。</span></p> 
<h2>TOML 插件捆绑</h2> 
<p>PyCharm 2022.1 EAP 2 捆绑了 TOML 插件，可以开箱即用地处理 TOML 文件。</p> 
<p> </p> 
<p>除了上述变动外，PyCharm 2022.1 EAP 2 版本还有其他一些变更，详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fpycharm%2F2022%2F02%2F2022-1-eap-2%2F" target="_blank">官方博客</a>，或查看完整的版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FPY-A-233537925%2FPyCharm-2022.1-EAP-2-%28221.4165.171-build%29-Release-Notes" target="_blank">发行说明</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            