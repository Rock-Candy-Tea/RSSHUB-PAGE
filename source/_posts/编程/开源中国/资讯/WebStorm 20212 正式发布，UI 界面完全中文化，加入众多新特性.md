
---
title: 'WebStorm 2021.2 正式发布，UI 界面完全中文化，加入众多新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202107/28072020_WEGF.png'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 07:20:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202107/28072020_WEGF.png'
---

<div>   
<div class="content">
                                                                                            <p>WebStorm 2021.2 正式发布，更新内容如下：</p> 
<h2><strong>代码编辑</strong></h2> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/reload-pages-on-save-624@2x.png" src="https://static.oschina.net/uploads/img/202107/28072020_WEGF.png" referrerpolicy="no-referrer"></p> 
<h3>保存时重新加载页面</h3> 
<p>WebStorm 现在可以在编辑和保存你的 HTML、CSS 和 JavaScript 文件时自动更新浏览器中的页面。要开始使用，请在编辑器中打开一个 HTML 文件，将鼠标悬停在它上面，然后点击你想使用的浏览器的图标——所有浏览器都支持。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/actions-on-save-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072021_4TSk.png" referrerpolicy="no-referrer"></p> 
<h3>保存时的操作</h3> 
<p>你喜欢在保存时执行某些操作吗？WebStorm 2021.2 现在正确支持这一工作流程，我们重新设计了所有现有的功能，将其收集到一个地方，并通过一些新的选项来加强它，包括在保存时重新格式化代码和优化导入的能力。</p> 
<h3>更快地创建 scratch 文件</h3> 
<p>想在项目背景之外处理一些代码？在编辑器中选择它，然后按⌥⏎，并选择从选择中创建新的 scratch 文件。这将创建一个带有所需代码的 scratch 文件。</p> 
<h3>Code With Me</h3> 
<p>当你在 Code With Me 会话中处于跟随模式时，你现在可以跟踪你所跟随的人使用的代码完成建议。</p> 
<h2><strong>JavaScript & TypeScript</strong></h2> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/auto-imports-for-commonjs-624@2x.png" src="https://static.oschina.net/uploads/img/202107/28072021_CPef.png" referrerpolicy="no-referrer"></p> 
<h3>自动导入 <code>require()</code></h3> 
<p>WebStorm 可以在你完成 ES6 符号时添加缺少的导入语句，它现在也可以为 CommonJS 模块做同样的事情 —— require 导入可以在代码补全时插入。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/support-for-ts-types-in-jsdoc-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072021_E3hA.png" referrerpolicy="no-referrer"></p> 
<h3>在 JSDoc 中支持 TypeScript 类型</h3> 
<p>WebStorm 现在正确地支持 .js 文件中使用的 TypeScript 语法。我们重新设计并扩展了现有的支持，并修复了许多已知的问题。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/surround-with-arrow-function-template-624@2x.png" src="https://static.oschina.net/uploads/img/202107/28072021_Y44t.png" referrerpolicy="no-referrer"></p> 
<h3>箭头函数的新操作</h3> 
<p>需要在你的代码中快速添加一个箭头函数？现在你可以使用 ⌥⌘J 将一个代码块用一个箭头函数包围。你也可以输入 arf 并按下 ⇥ 来展开模板并添加一个空的箭头函数。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/preview-tab-in-debugger-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072021_zRym.png" referrerpolicy="no-referrer"></p> 
<h3>调试时的预览选项页</h3> 
<p>预览选项页过去只在项目视图中起作用，现在当你调试你的应用程序时也起作用。可以在首选项/设置|编辑器|常规|编辑器标签中开启这个功能。这将帮助你避免用多个文件弄乱编辑器，因为 WebStorm 将在一个标签中连续打开这些文件。</p> 
<h2><strong>框架和技术</strong></h2> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/rename-refactoring-for-react-useState-hooks-624@2x.png" src="https://static.oschina.net/uploads/img/202107/28072022_nzmJ.png" referrerpolicy="no-referrer"></p> 
<h3>React useState hooks</h3> 
<p>你不再需要把时间浪费在逐一重构 useState 值和函数上—— WebStorm 现在可以为你重命名两者。将光标放在一个状态值上，然后按 ⇧F6 或者从右键菜单中进入 Refactor | Rename。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/completion-for-private-npm-packages-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072022_kIq2.png" referrerpolicy="no-referrer"></p> 
<h3>对类名和 clsx 库的支持</h3> 
<p>为了帮助你在 React 项目中更有效地使用 CSS 类，我们增加了对流行的类名和 clsx 库的支持。WebStorm 将显示你的CSS类的补全建议，并解决字符串字面和属性中所有带有字面名称的符号。</p> 
<h3>对网络类型的通用支持</h3> 
<p>我们扩展了对 web-types 的支持，这是一个用于记录 web 框架的开源标准。它以前主要是对 Vue 的支持。但现在你可以用它来丰富你的 HTML 文件中自定义组件的编码帮助。</p> 
<h2><strong>版本控制</strong></h2> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/run-tests-before-commit-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072022_YNi9.png" referrerpolicy="no-referrer"></p> 
<h3>新的预提交检查</h3> 
<p>WebStorm 增加了一个新的选项，让用户在提交之前运行测试来检查代码。点击提交工具窗口中的齿轮图标，选择运行测试，并选择所需的运行配置。WebStorm 将测试你的文件并对任何问题发出警告。</p> 
<h3>GPG 签名支持</h3> 
<p>现在你可以通过用 GPG 密钥签名来保护你的提交。你可以通过首选项/设置|版本控制|Git 中的配置 GPG 密钥，来开启这个功能。</p> 
<h3>本地历史搜索</h3> 
<p>查看本地历史中的修订版现在更容易了。在已修改的文件上点击右键，然后进入本地历史|显示历史，并使用搜索栏来浏览你的修改。</p> 
<h2><strong>可用性</strong></h2> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/language-pack-plugins-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072022_3g8S.png" referrerpolicy="no-referrer"></p> 
<h3>本地化的用户界面</h3> 
<p>从这个版本开始，你可以享受完全本地化的中文、韩文和日文的 WebStorm 用户界面。本地化可作为非捆绑式语言包插件使用，可以在 WebStorm 中从首选项/设置|插件中安装。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/drag-drop-tool-windows-624@2x.png" src="https://static.oschina.net/uploads/img/202107/28072022_k0U3.png" referrerpolicy="no-referrer"></p> 
<h3>更快的工具窗口重新排列</h3> 
<p>现在更容易重新排列工具窗口了。将鼠标悬停在你想移动的工具窗口的顶部，然后将它拖到你想要的地方即可。如果你想把一个工具窗口从 WebStorm 主窗口中分离出来，也可以这样做 —— 只要把它拖到 IDE 框架之外即可。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/customize-project-icon-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072023_gNe3.png" referrerpolicy="no-referrer"></p> 
<h3>更加容易地定制项目图标</h3> 
<p>WebStorm 让用户为项目分配自定义图标这个过程变得更加简单了。在 WebStorm 的欢迎屏幕上右击一个项目，然后选择更改项目图标选项，并上传你想与该项目相关联的 SVG 文件。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/update-notification-from-toolbox-app-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072023_5XUN.png" referrerpolicy="no-referrer"></p> 
<h3>从工具箱应用程序中更新通知</h3> 
<p>你将不再错过工具箱应用程序的任何关键产品更新。如果有新的版本可供下载，WebStorm 会通知你，并让你选择升级到该版本 —— 只要确保你有 1.20.8804 或更高版本的 Toolbox App。</p> 
<p><img alt="https://www.jetbrains.com/webstorm/whatsnew/img/2021.2/updated-preferences-in-ws-810@2x.png" src="https://static.oschina.net/uploads/img/202107/28072023_vmi0.png" referrerpolicy="no-referrer"></p> 
<h3>改进的首选项/设置对话框</h3> 
<p>在你的首选项/设置对话框中，现在有一个高级设置的节点。你可以在那里找到一些新的配置选项，包括在无干扰模式下设置左边距的功能。另外，你现在可以在最近打开的节点之间更快地跳转 —— 只需使用对话框右上角的箭头。</p> 
<h3>自动缓存和日志清理</h3> 
<p>在每次重大更新后，WebStorm 都会清理最后一次更新超过 180 天的任何缓存和日志目录。系统设置和插件目录将保持原样。要手动触发这个过程，请到主菜单中的 帮助|删除遗留的 IDE 目录 进行设置。</p> 
<h3>内置终端的新功能</h3> 
<p>内置终端添加了三个新功能，以改善使用体验。你现在可以改变光标的形状，并使 ⌥ 键作为元修饰符 —— 在首选项/设置|工具|终端中寻找这些选项。另外，现在使用 http 链接也更方便了。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fwebstorm%2Fwhatsnew%2F%3Frss" target="_blank">https://www.jetbrains.com/webstorm/whatsnew/?rss</a></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            