
---
title: 'GoLand 2022.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202207/31072653_ljq9.png'
author: 开源中国
comments: false
date: Sun, 31 Jul 2022 07:27:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202207/31072653_ljq9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GoLand 2022.2 为泛型和 <code>go.work</code> 带来了新功能，还增加了对模糊测试的支持，SQL 语句现在可被自动检测，还带来了针对它们的全面代码辅助。</p> 
<p>GoLand 现已支持 WebSocket 连接，并且可以通过 HTTP 和 WebSocket 协议发送 GraphQL 查询。</p> 
<h2>泛型</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/interface-any.png" src="https://static.oschina.net/uploads/img/202207/31072653_ljq9.png" referrerpolicy="no-referrer"></p> 
<h3>将空接口转换为 <code>any</code> 的意图操作</h3> 
<p>GoLand 的新增检查可以将空接口的用法报告为类型或类型约束。</p> 
<p>另一个意图操作是将 <code>interface&#123;&#125;</code> 替换为 <code>any</code>。 从意图操作的弹出窗口中，您可以替换文件中的所有空接口。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/empty-list-params.png" src="https://static.oschina.net/uploads/img/202207/31072654_udV4.png" referrerpolicy="no-referrer"></p> 
<h3>将具有空形参列表的类型形参删除的快速修复</h3> 
<p>具有空形参列表的类型形参现在报告为错误，并添加了将其删除的快速修复。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/unused-type-parameter.png" src="https://static.oschina.net/uploads/img/202207/31072654_J7Nm.png" referrerpolicy="no-referrer"></p> 
<h3>对未使用的类型形参的检查</h3> 
<p>GoLand 2022.2 添加了一项可以报告未使用的类型形参的新检查。它们将被灰显，将鼠标悬停到它们上面时，你会看到警告。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/union-interface-with-methods.png" src="https://static.oschina.net/uploads/img/202207/31072654_JqI2.png" referrerpolicy="no-referrer"></p> 
<h3>对接口与方法的联合的检查</h3> 
<p>如果你尝试将接口与方法在联合中一起使用，IDE 现在会报告错误。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/type-parameter-constraint.png" src="https://static.oschina.net/uploads/img/202207/31072655_ESt8.png" referrerpolicy="no-referrer"></p> 
<h3>对将类型形参用作约束的检查</h3> 
<p>如果尝试将类型形参用作约束，GoLand 将显示错误。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/completion-method-receiver.png" src="https://static.oschina.net/uploads/img/202207/31072655_ZcXS.png" referrerpolicy="no-referrer"></p> 
<h3>输入方法的接收器时对类型形参的补全</h3> 
<p>在方法创建期间添加接收器时，GoLand 会自动插入类型形参的标识符。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/new-find-usages-generics.png" src="https://static.oschina.net/uploads/img/202207/31072655_uFUv.png" referrerpolicy="no-referrer"></p> 
<h3>类型形参的新 Find Usages（查找用法）组</h3> 
<p>GoLand 2022.2 为泛型引入了新的 Find Usages（查找用法）组：类型形参声明。</p> 
<h2>模糊测试</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/fuzz.png" src="https://static.oschina.net/uploads/img/202207/31072656_LuHV.png" referrerpolicy="no-referrer"></p> 
<h3>运行模糊测试</h3> 
<p>现在可以从 GoLand 运行模糊测试。 如果您点击模糊测试旁间距中的绿色三角形图标，将看到运行测试的不同选项。 如果测试失败，失败的种子语料库条目将被写入文件并置于 <code>testdata</code> 文件夹的软件包目录中。</p> 
<p>此文件的路径也将作为可点击链接出现在控制台中。 如果点击此链接，文件将在 IDE 中打开，文件顶部将显示绿色三角形图标。 点击此图标将运行 <code>go test</code> 并显示失败的种子语料库条目。</p> 
<p>从 GoLand 也可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.dev%2Fdoc%2Ffuzz%2F%23running-fuzz-tests" target="_blank">像普通单元测试一样</a>运行模糊测试。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/fuzz-quick-fix.png" src="https://static.oschina.net/uploads/img/202207/31072656_uyQS.png" referrerpolicy="no-referrer"></p> 
<h3>更改 Go SDK 的快速修复</h3> 
<p>在 GoLand 中，如果配置了不支持模糊测试的 Go SDK，间距中将不再显示运行按钮。GoLand 2022.2 添加了一个快速修复，它可以在当前 Go SDK 不支持模糊测试时更改 Go SDK。</p> 
<h2>Go 工作区</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/gowork.png" src="https://static.oschina.net/uploads/img/202207/31072656_FsKz.png" referrerpolicy="no-referrer"></p> 
<h3>对多条 <code>use</code> 指令进行分组的快速修复</h3> 
<p>添加了一个快速修复，它可以将 <code>go.work</code> 文件中的多条 <code>use</code> 指令组合到一条指令中。</p> 
<h2>Go 1.19</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/appendf.png" src="https://static.oschina.net/uploads/img/202207/31072657_ZTfB.png" referrerpolicy="no-referrer"></p> 
<h3>对 <code>fmt.Appendf</code> 的支持</h3> 
<p>添加了对 <code>fmt.Appendf</code> 的支持，GoLand 现在可以识别字符串中的格式设置动词。 因此，<code>Appendf</code> 函数可以利用格式设置函数具有的所有功能，例如 <em>Add a format string argument</em>（添加格式字符串实参）意图操作。</p> 
<h3>对 <code>unix</code> 构建约束的支持</h3> 
<p>GoLand 现已支持新的 <code>unix</code> 构建标记，后者可以识别任何 Unix 或类 Unix 系统。</p> 
<h3><code>loong64</code> 加入 <em>Arch</em> 列表</h3> 
<p>Go 1.19 引入了新架构 <code>loong64</code>。 我们已将其添加到 <em>Preferences</em> | <em>Go</em> | <em>Build Tags & Vendoring</em>（设置 | Go | 构建标记和 Vendoring）下的 <em>Arch</em> 列表中。</p> 
<h2>快速文档</h2> 
<p>改进了 <em>Quick Documentation</em>（快速文档）：</p> 
<ul> 
 <li>GoLand 现在会为 25 个 Go 关键字中的每一个显示有意义的关键字工具提示，概述相关关键字的语义。</li> 
 <li>现在会显示通道方向信息。此数据在三个位置的工具提示中显示：将鼠标悬停在 <code>chan</code> 关键字上时、通道进行发送和接收操作时以及对通道类型的所有引用上。</li> 
 <li><code>iota</code> 的 Quick Documentation（快速文档）现在包含有关使用方式的额外信息。 如果常量是 <code>iota</code> 组的一部分，则值现在会显示在补全框中，即使常量是隐式定义的。</li> 
 <li>另有一个新的工具提示解释了类型 switch 的运作方式。</li> 
 <li>如果在类型形参上调用 <em>Quick Documentation</em>（快速文档），GoLand 将显示工具提示，简要说明泛型如何工作并提供 Go 团队教程的链接。</li> 
 <li>类型断言的工具提示现在包含额外相关信息并提供了示例。</li> 
 <li>如果将鼠标悬停在大括号内的区域上，在你初始化映射、数组、切片和结构时，GoLand 会显示额外信息。</li> 
 <li>将鼠标悬停在空白标识符上时，GoLand 会显示工具提示，解释空白标识符及其运作方式。</li> 
</ul> 
<h2>更多 Go 相关改进</h2> 
<h3>性能优化</h3> 
<p>GoLand 不再扫描 <code>~/go/pkg/mod</code> 中的 <code>cache</code> 子目录，因为后者不包含 IDE 正常运行所需的信息。 这个文件夹可能相当大，将其从扫描中排除应该可以提高性能。</p> 
<h3>对 <code>go:linkname</code> 指令的支持</h3> 
<p>添加了对 <code>go:linkname</code> 编译器指令的支持：</p> 
<p><code>//go:linkname localname [importpath.name]</code></p> 
<p>它会指示编译器使用 <code>importpath.name</code> 作为在源代码中声明为 <code>localname</code> 的变量或函数的对象文件符号名称。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/iota-irregular.png" src="https://static.oschina.net/uploads/img/202207/31072657_xZ8A.png" referrerpolicy="no-referrer"></p> 
<h3><code>iota</code> 非常规用法检查</h3> 
<p>GoLand 中新增了一项检查，如果 <code>iota</code> 的用法不合常规，检查会发出警告。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/iota-reserved.png" src="https://static.oschina.net/uploads/img/202207/31072657_fkAk.png" referrerpolicy="no-referrer"></p> 
<p>还为 <code>iota</code> 和其他内置常量启用了 <em>Reserved word used as name</em>（保留词用作名称）检查。 尝试对名为 <code>iota</code>、<code>true</code> 或 <code>false</code> 的常量分配值时，将触发检查。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/value-pointer-receivers.png" src="https://static.oschina.net/uploads/img/202207/31072657_Czab.png" referrerpolicy="no-referrer"></p> 
<h3>对值和指针接收器上的方法的检查</h3> 
<p>Go 文档建议给定类型上的所有方法都应该有值或指针接收器。</p> 
<p>GoLand 中新增了一项检查，如果类型在值和指针接收器上都有方法，检查会发出警告。</p> 
<h2>自动 SQL 检测</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/sql.png" src="https://static.oschina.net/uploads/img/202207/31072658_oAv8.png" referrerpolicy="no-referrer"></p> 
<p>SQL 语句现在可被自动检测 ，语言将被注入到与特定模式匹配的每个字符串文字。 将语言注入字符串文字时，如果编辑该文字，您将获得全面的代码辅助。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/sql-detection-settings.png" src="https://static.oschina.net/uploads/img/202207/31072658_KXgV.png" referrerpolicy="no-referrer"></p> 
<p>可以在 <em>Preferences</em> | <em>Editor</em> | <em>Language Injections</em>（设置 | 编辑器 | 语言注入）中查找、编辑模式以及添加自己的模式。</p> 
<h2>运行任何内容</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/run-anything.png" src="https://static.oschina.net/uploads/img/202207/31072658_KxfS.png" referrerpolicy="no-referrer"></p> 
<p>GoLand 现在支持 <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Frunning-anything.html" target="_blank">Run Anything</a></em>（运行任何内容）操作，你可以使用它快速启动运行/调试配置、应用程序、脚本、命令和任务，以及打开最近的项目。 只需按两次 ^ 并在搜索栏中输入所需内容即可。</p> 
<h2>HTTP 客户端</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/websocket.png" src="https://static.oschina.net/uploads/img/202207/31072659_M0Jp.png" referrerpolicy="no-referrer"></p> 
<h3>对 WebSocket 端点的支持</h3> 
<p>GoLand 现在支持 WebSocket 连接。 您可以创建请求以及发送和接收消息。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/graphql.png" src="https://static.oschina.net/uploads/img/202207/31072659_a5Bu.png" referrerpolicy="no-referrer"></p> 
<h3>对 GraphQL 端点的支持</h3> 
<p>GoLand 现在可以原生通过 HTTP 和 WebSocket 协议发送 GraphQL 查询。 对于 <code>http://</code> 和 <code>https://</code>，使用的是简单的 HTTP 请求，<code>ws://</code> 和 <code>wss://</code> 则被委托给 WebSocket 执行器。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/select-run-environment.png" src="https://static.oschina.net/uploads/img/202207/31072659_hoar.png" referrerpolicy="no-referrer"></p> 
<h3>选择运行环境</h3> 
<p>现在，在间距的播放图标上可以通过新方式选择运行环境。 要启用此功能，请从 <em>Run with</em>（运行方式）组合框中选择 <em>Select Environment Before Run</em>（运行前选择环境）选项。</p> 
<h2>远程开发</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/remdev.png" src="https://static.oschina.net/uploads/img/202207/31072700_N0mq.png" referrerpolicy="no-referrer"></p> 
<p>更新了 GoLand <em>欢迎</em>屏幕的 <em>Remote Development</em>（远程开发）版块。 在这里，您可以为后端编排选择首选方法。 此外，端口转发功能现在可用于终端上运行的进程。</p> 
<h2>Space</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/space.png" src="https://static.oschina.net/uploads/img/202207/31072700_No3b.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fzh-cn%2Fspace%2F" target="_blank">JetBrains Space</a> 是一个完整的软件开发平台，在整个开发环境为 JetBrains IDE 提供项目管理、问题跟踪、Git 托管、代码审查、持续集成、软件包仓库和远程后端编排。</p> 
<p>Space 集成现与 GoLand 捆绑。 借助这种一流集成，你可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fspace%2Fspace-plugin-for-ide.html%23view-and-clone-repositories" target="_blank">浏览 Space 项目</a>并克隆仓库，然后直接开始工作。当更改就绪后，你可以在 IDE 中创建合并请求并执行代码审查。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/space-rem-dev.png" src="https://static.oschina.net/uploads/img/202207/31072700_EKHP.png" referrerpolicy="no-referrer"></p> 
<p>现在可以直接在 GoLand 中管理用于远程开发的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fzh-cn%2Fremote-development%2Fspace-dev-environments%2F" target="_blank">Space 开发环境</a></p> 
<p>当 IDE 关联到 Space 组织时，所有现有开发环境都会同步。 可以为仓库和分支创建新的开发环境，并立即开始编码。 可以将开发环境休眠以减少资源消耗，或者在工作完成后直接将其删除。</p> 
<h2>用户界面</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/merge-windows.png" src="https://static.oschina.net/uploads/img/202207/31072700_YysK.png" referrerpolicy="no-referrer"></p> 
<h3>macOS 上的 Merge All Project Windows（合并所有项目窗口）操作</h3> 
<p>为 macOS 用户引入了一项功能，利用此功能可以将所有打开的项目窗口合并成一个，将其变成选项卡。 转到 <em>Window</em> | <em>Merge All Project Windows</em>（窗口 | 合并所有项目窗口）即可启用。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/shortcut-font-size.png" src="https://static.oschina.net/uploads/img/202207/31072701_o3Lp.png" referrerpolicy="no-referrer"></p> 
<h3>更改字体大小的键盘快捷键</h3> 
<p>引入了一个键盘快捷键，它可以更改编辑器中所有位置的字体大小。 要增大字体，请按 ⌃⇧.。要减小字体，请按 ⌃⇧,</p> 
<p>在编辑器中放大或缩小代码时，现在可以看到显示当前字体大小的指示器以及将其恢复为默认值的选项。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/mnemonic-bookmark.png" src="https://static.oschina.net/uploads/img/202207/31072701_rxnc.png" referrerpolicy="no-referrer"></p> 
<h3>助记书签的新 Description（描述）字段</h3> 
<p>已将 <em>Description</em>（描述）字段集成到 <em>Add Mnemonic Bookmark</em>（添加助记书签）对话框中，因此，可以为书签添加可选描述。要添加助记书签，请右键点击要添加书签的行旁边的间距，然后从上下文菜单中选择相应选项。 或者使用快捷键 ⌥F3。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/cloning-progress-bar.png" src="https://static.oschina.net/uploads/img/202207/31072701_7rES.png" referrerpolicy="no-referrer"></p> 
<h3>Cloning repository（正在克隆仓库）进度条</h3> 
<p><em>Cloning repository</em>（正在克隆仓库）进度条现在直接显示在 <em>Projects</em>（项目）列表中。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/faster-completion-settings.png" src="https://static.oschina.net/uploads/img/202207/31072702_TqTC.png" referrerpolicy="no-referrer"></p> 
<h3>更快访问 Code Completion Settings（代码补全设置）</h3> 
<p>现在可以从代码补全弹出窗口的垂直省略号菜单按钮访问 <em>Code Completion Settings</em>（代码补全设置）。</p> 
<h2>编辑器</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/control-parentheses.png" src="https://static.oschina.net/uploads/img/202207/31072702_ItWs.png" referrerpolicy="no-referrer"></p> 
<h3>控制自动圆括号插入</h3> 
<p>我们添加了一个选项，可用于切换 IDE 在代码补全期间是否自动插入圆括号。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/inspections-highlighting.png" src="https://static.oschina.net/uploads/img/202207/31072702_gCMI.png" referrerpolicy="no-referrer"></p> 
<h3>更改检查的高亮显示样式</h3> 
<p>可以使用 <em>Preferences</em> | <em>Editor</em> | <em>Inspections</em>（设置 | 编辑器 | 检查）中的新 <em>Highlighting in editor</em>（编辑器中的高亮显示）下拉菜单调整检查的高亮显示样式。</p> 
<p>这为你提供了更多用于自定义检查的选项。 例如，可以将特定检查的严重性级别设为 <em>Warning</em>（警告），但将高亮显示样式更改为 <em>Error</em>（错误）。</p> 
<h2>Docker</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/copy-image.png" src="https://static.oschina.net/uploads/img/202207/31072703_1fT5.png" referrerpolicy="no-referrer"></p> 
<h3>复制 Docker 镜像</h3> 
<p>现在可以使用新的 <em>Copy Docker Image</em>（复制 Docker 镜像）操作将镜像从一个 Docker 守护进程复制到另一个，该操作会将镜像保存到文件中，然后将其推送到所选连接。</p> 
<h3>IDE 重启时 Docker 自动连接</h3> 
<p>现在，重新启动 IDE 后，GoLand 会自动连接到 Docker。 这一新设置在 <em>Preferences</em> | <em>Advanced Settings</em> | <em>Docker</em>（设置 | 高级设置 | Docker）中默认启用。</p> 
<h3>与 Colima 和 Rancher 的集成</h3> 
<p>GoLand 现在与 Colima 和 Rancher 集成，支持更多用于建立与 Docker 守护进程的连接的选项。</p> 
<h2>数据库</h2> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/import-multiple-csv.png" src="https://static.oschina.net/uploads/img/202207/31072703_MDrv.png" referrerpolicy="no-referrer"></p> 
<h3>导入多个 CSV 文件的选项</h3> 
<p>现在可以选择多个 CSV 文件并一次全部导入。</p> 
<p><img alt="https://www.jetbrains.com/go/whatsnew/img/2022.2/database-resolve-modes.png" src="https://static.oschina.net/uploads/img/202207/31072703_PXej.png" referrerpolicy="no-referrer"></p> 
<h3>数据库的解析模式</h3> 
<p>使用数据库时，现在拥有<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fdatagrip%2F2022%2F06%2F20%2Fdatagrip-2022-2-eap-2%2F" target="_blank">两种文件解析模式</a>：<em>Playground</em>（演练场）和 <em>Script</em>（脚本）。</p> 
<p><em>Playground</em>（演练场）适用于有一组未连接查询的情况，而 <em>Script</em>（脚本）适用于具有顺序逻辑的查询。</p> 
<h2>其他改进</h2> 
<h3>导入受信任的 SSL 证书</h3> 
<p>GoLand 现在可以帮助您从系统受信任存储区导入受信任的 SSL 证书。 它将自动使用特定于企业环境的自定义证书。 您无需执行任何其他操作。 一切都开箱即用。</p> 
<h3>JSON 和 YAML 文件中的可点击 URL</h3> 
<p>JSON 和 YAML 文件现在会在以 <code>http://</code> 和 <code>https://</code> 开头的值中自动插入 Web 引用。 您可以在 Web 浏览器中打开这些链接并在 HTTP 客户端中生成请求。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2022%2F07%2F28%2Fgoland-2022-2-is-here%2F" target="_blank">https://blog.jetbrains.com/go/2022/07/28/goland-2022-2-is-here/</a></p>
                                        </div>
                                      
</div>
            