
---
title: 'PyCharm 2021.3 已发布，提供 Poetry  和 FastAPI 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c45aaa8d047f6d007f622f706dc695b94ce.png'
author: 开源中国
comments: false
date: Sat, 04 Dec 2021 07:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c45aaa8d047f6d007f622f706dc695b94ce.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px"><span style="color:#19191c">PyCharm 2021.3 已发布，此版本终止对 Mako、Buildout 和 Web2Py 的支持，同时带来了一些新特性：</span></p> 
<h3><span style="color:#19191c">Poetry 支持</span></h3> 
<p style="margin-left:0px"><span style="color:#19191c">PyCharm 现在支持 Poetry ，并为 <em>pyproject.toml </em>文件提供开箱即用的代码补全功能。</span></p> 
<p style="margin-left:0px"><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-c45aaa8d047f6d007f622f706dc695b94ce.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px"><span style="color:#19191c">此外，PyCharm 现在支持 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0612%2F" target="_blank"><span style="color:#19191c">PEP 612 - 参数规范变量</span></a><span style="color:#19191c">，这是 Python 3.10 中的另一个新功能。</span></p> 
<h2><span style="color:#19191c">Web 开发（pro）</span></h2> 
<h3><span style="color:#19191c"><span style="background-color:#ffffff">FastAPI 支持</span></span></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffastapi.tiangolo.com%2F" target="_blank"><span style="color:#19191c">FastAPI</span></a><span style="color:#19191c"> 是一种流行的用于构建 API 的高性能 Python Web 框架，现在在 PyCharm 中得到支持。选择 FastAPI 项目类型，让 PyC​​harm 安装所有依赖项，然后创建运行/调试配置。<span style="background-color:#ffffff">或者，也可以使用 PyCharm 打开现有 FastAPI 项目并自行创建 FastAPI 运行配置。 PyCharm 将检测应用程序并运行 Uvicorn。</span></span></p> 
<p><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-2e8f63cd5778e4e52a3e714b4a95bbbbca7.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#19191c">现在可以更轻松地使用“test.http”文件来测试 HTTP 端点，直接从编辑器将 GET、POST 和其他请求类型发送到应用程序端点。</span></p> 
<p><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-a774bb31402cda3cab4abc214b1fa376aa7.png" width="700" referrerpolicy="no-referrer"></span></p> 
<h3><span style="color:#19191c"><span style="background-color:#ffffff">FastAPI 和 Flask 的新端点工具窗口</span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#19191c">因此 PyCharm 2021.3 为 FastAPI 和 Flask 项目类型引入了新的 <em>Endpoints</em>（端点）工具窗口。</span></p> 
<p style="color:rgba(25, 25, 28, 0.7); margin-left:0px; margin-right:0px; text-align:start"><span style="color:#19191c">开始处理新项目或现有项目后，PyCharm 将扫描路由并将其列在 <em>Endpoints</em>（端点）工具窗口中，您可以在该窗口中对 URL 进行代码补全、导航和重构。 此工具窗口还提供了对端点的更好概览和对文档的快速访问。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-8e94daa0ba1908954ac1120b120352a0731.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
<h3><span style="color:#19191c"><span style="background-color:#ffffff">其他改进：</span></span></h3> 
<div> 
 <ul> 
  <li><span style="color:#19191c">PyCharm 不再要求使用“<”开始 HTML 标记来获取代码补全建议。</span></li> 
  <li><span style="color:#19191c">现在可以使用新的 <em>Update ‘package name’ to the latest version</em>（将“软件包名称”更新到最新版本）检查直接从编辑器将 package.json 文件中的 npm 软件包更新到最新版本。</span></li> 
  <li><span style="color:#19191c">输入 URL 并使用 ES6 文件中导入路径的快速修复下载远程 ES6 模块。</span></li> 
 </ul> 
 <h2><span style="color:#19191c"><span style="background-color:#ffffff">全新 Jupyter Notebook 体验</span></span></h2> 
 <h3><span style="color:#19191c"><span style="background-color:#ffffff">新的 Jupyter Notebook 界面</span></span></h3> 
 <p><span style="color:#19191c"><span style="background-color:#ffffff">Notebook 支持现在更加流畅。 PyCharm 现在原生提供经典 Jupyter Notebook UI，同时包含 IDE 中的所有强大工具，包括自动导入、代码补全和重构功能。</span></span></p> 
 <p><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-7416e67a79230573dd98b4403e55b1c9e51.png" width="700" referrerpolicy="no-referrer"></span></p> 
 <h3><span style="color:#19191c"><span style="background-color:#ffffff">热门快捷方式</span></span></h3> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">添加了对所有标准 Jupyter 快捷方式的支持，包括使用 <em>shift+enter </em>运行单元格、通过单击在命令和编辑器模式之间切换、使用箭头键在单元格上导航等等</span></span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-c1b33f1b0e595cc4f8d351c3db4b044eaa6.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
  <h3><span style="color:#19191c"><span style="background-color:#ffffff">交互式输出</span></span></h3> 
  <div> 
   <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">PyCharm Pro 现在完全支持流行的科学库（如 Plotly、Bokeh、Altair、ipywidgets 等）使用的静态或基于 JavaScript 的输出，以及对 DataFrames 的丰富支持。</span></span></p> 
   <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-835d1a651b1fd7b58c7845dfb2f42418e3a.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
   <p style="margin-left:0; margin-right:0"> </p> 
   <h3><span style="color:#19191c"><span style="background-color:#ffffff">调试能力</span></span></h3> 
   <div> 
    <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">在 Jupyter notebook 中进行调试，停在断点处、单步执行代码、浏览和管理变量的状态等等。</span></span></p> 
    <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-b0eac3740c95f1128da323ffa022132b067.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
    <h2><span style="color:#19191c"><span style="background-color:#ffffff">远程开发 （<span style="background-color:var(--wt-color-primary-light-theme)">BETA、</span><span style="background-color:var(--wt-color-error)">PRO）</span></span></span></h2> 
    <div> 
     <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">PyCharm Pro 现在通过 JetBrains Gateway 支持远程开发工作流的测试版。PyCharm 用户可以从世界任何地方连接到远程机器，运行 PyCharm 的后端，可以在本地运行的同时利用远程计算能力。</span></span></p> 
     <p style="margin-left:0px; margin-right:0px"><span style="color:#19191c"><span style="background-color:#ffffff">要试用它，只需单击 <strong><em>欢迎屏幕</em>上的<em>远程开发</em>，选择</strong><em><strong>SSH 选项</strong> </em>并按照向导提供凭据，建立连接，然后在服务器上下载 IDE。</span></span></p> 
     <p style="margin-left:0px; margin-right:0px"><span style="background-color:#ffffff"><span style="color:#19191c">此功能处于测试阶段，有关更多详细信息，请参阅 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fpycharm%2F2021.3%2Fremote-development-starting-page.html" target="_blank"><span style="color:#19191c">文档</span></a><span style="color:#19191c">。</span></span></p> 
     <p style="margin-left:0px; margin-right:0px"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-8db199961f63e33f6f7995e0b8caa830302.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
     <h2><span style="color:#19191c"><span style="background-color:#ffffff">用户体验改进</span></span></h2> 
     <h3><span style="color:#19191c"><span style="background-color:#ffffff">下载流行 Python Packages （<span style="background-color:var(--wt-color-error)">PRO） 的</span>共享索引</span></span></h3> 
     <p><span style="color:#19191c">PyPI 上流行的软件包（例如 Numpy、Pandas、Matplotlib、Sqlalchemy、Scikit-image、Plotly、Scipy 等）的用户现在可以下载预构建的索引，以加快 IDE 索引时间。这些共享索引不包含在 PyCharm 安装中，因此 IDE 将在下载任何索引之前请求许可。</span></p> 
     <p><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-4fc9eb137713b694f7ab220d8a34c1a6af9.png" width="700" referrerpolicy="no-referrer"></span></p> 
     <h3><span style="color:#19191c"><span style="background-color:#ffffff">拆分运行工具窗口</span></span></h3> 
     <div> 
      <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">现在可以将“<em>运行”</em>工具窗口拆分为多个选项卡，这样就可以同时运行多个配置，同时仍能访问其结果。只需将选项卡拖放到 “<em>运行” </em>工具窗口内的突出显示区域即可将其拆分。</span></span></p> 
      <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt src="https://oscimg.oschina.net/oscnet/up-1427efbaa664d932281cd2eba8c10139ef4.gif" width="700" referrerpolicy="no-referrer"></span></span></p> 
      <h3><span style="color:#19191c"><span style="background-color:#ffffff">功能培训师：新的入门教程</span></span></h3> 
      <p><span style="color:#19191c"><span style="background-color:#ffffff">如果您是 PyCharm 的新手，或者想重新了解使用方法，IDE Features Trainer 现在提供了入门导览和有关 PyCharm 中 Git 功能的课程。</span></span></p> 
      <p><span style="color:#19191c"><span style="background-color:#ffffff">要开始尝试，请点击欢迎屏幕上的“Learn PyCharm”（学习 PyCharm）或点击 IDE 主菜单中的 </span><em>Help > Learn IDE</em><span style="background-color:#ffffff">（帮助 > 学习 IDE）。</span></span></p> 
      <p><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-8b166224afb8b3cb96f906d8ba8e63b97ec.png" width="700" referrerpolicy="no-referrer"></span></p> 
      <h3><span style="color:#19191c"><span style="background-color:#ffffff">评估来自调试器的表达式</span></span></h3> 
      <div> 
       <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">在此版本中，</span><em>Evaluate</em><span style="background-color:#ffffff">（评估）功能的曝光度得到改进。 现在可以在 </span><em>Debug</em><span style="background-color:#ffffff">（调试）工具窗口中快速访问 </span><em>Evaluate</em><span style="background-color:#ffffff">（评估）字段，而不必使用监视。</span></span></p> 
       <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-50bc5030c3ceb17d674206c67f86f65b565.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
       <p style="margin-left:0; margin-right:0"> </p> 
       <h3><span style="color:#19191c"><span style="background-color:#ffffff">进一步改进：</span></span></h3> 
       <div> 
        <ul> 
         <li><span style="color:#19191c">可以在索引编制期间创建和编辑运行配置。</span></li> 
         <li><span style="color:#19191c">在 Python 软件包的安装过程中可以更详细地了解失败信息，从而更好地修正意外问题。</span></li> 
         <li><span style="color:#19191c">可以停止 PyCharm 在 Markdown 列表中的自动编号和缩进下一行。 转到 <em>Preferences/Settings > Languages & Frameworks > Markdown</em>（偏好设置/设置 > 语言和框架 > Markdown），禁用 <em>Automatic assistance in the editor</em>（编辑器中的自动辅助）。</span></li> 
         <li><span style="color:#19191c">现在可以在 Python 控制台中将多个单元添加到执行队列。 PyCharm 在前一次执行完成之前不会再阻止你的操作。</span></li> 
         <li><span style="color:#19191c">现在可以在 <em>Preferences/Settings | Tools | SSH Configurations</em>（偏好设置/设置 | 工具 | SSH 配置）下为 SSH 配置指定 HTTP 或 SOCKS 代理服务器。</span></li> 
        </ul> 
        <h2><span style="color:#19191c"><span style="background-color:#ffffff">版本控制</span></span></h2> 
        <h3><span style="color:#19191c"><span style="background-color:#ffffff">重新组织的版本控制设置</span></span></h3> 
        <div> 
         <p style="color:rgba(25, 25, 28, 0.7); margin-left:0; margin-right:0; text-align:start"><span style="color:#19191c">重新组织了 VCS 设置，使其更加醒目。 在 <em>Preferences / Settings | Version Control</em>（偏好设置 / 设置 | 版本控制）中，可以找到所有可用设置的列表，这些设置作为配置 VCS 的起点。</span></p> 
         <p style="color:rgba(25, 25, 28, 0.7); margin-left:0px; margin-right:0px; text-align:start"><span style="color:#19191c">这些部分中的设置按最重要的进程组织：<em>Commit</em>（提交）、<em>Push</em>（推送）和 <em>Update</em>（更新）。 <em>Directory mappings</em>（目录映射）获得了单独的节点，后台操作默认开启。</span></p> 
         <p style="margin-left:0px; margin-right:0px"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-37f14663e1afe18060cdd27080abc4e8873.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
         <p style="margin-left:0px; margin-right:0px"> </p> 
         <h3><span style="color:#19191c">远程分支的 <em>Checkout and Rebase onto Current</em>（签出并变基到当前分支）</span></h3> 
         <div> 
          <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">如果需要签出所选分支并将其变基到当前签出的分支之上，现在可以使用 </span><em>Checkout and Rebase onto Current</em><span style="background-color:#ffffff">（签出并变基到当前分支）操作。</span></span></p> 
          <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">该操作此前仅适用于本地分支。 在 PyCharm 2021.3 中，您也可以将其用于远程分支。</span></span></p> 
          <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-a43bf142850c14a1c4475c21176bc0f9c12.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
          <h3><span style="color:#19191c"><span style="background-color:#ffffff">“</span><em>Push all up to here</em><span style="background-color:#ffffff">” 操作选项</span></span></h3> 
          <p><span style="color:#19191c"><span style="background-color:#ffffff">新的 </span><em>Push all up to here</em><span style="background-color:#ffffff">（推送此前所有提交）操作允许您只推送当前确信的提交，将其他提交留待以后处理。 这将使你可以推送在 Git 工具窗口的 Log（日志）选项卡中所选及其之前的提交。 要使用此操作，首先右键点击停止处的提交，调用上下文菜单，然后选择新的 </span><em>Push All up to Here</em><span style="background-color:#ffffff">（推送此前所有提交）操作。</span></span></p> 
          <h3><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-96ca456590846681f57b29a2c84e9469922.png" width="700" referrerpolicy="no-referrer"></span></h3> 
          <h2><span style="color:#19191c"><span style="background-color:#ffffff">数据库（PRO）</span></span></h2> 
          <h3><span style="color:#19191c"><span style="background-color:#ffffff">新的数据库差异窗口</span></span></h3> 
          <div> 
           <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">上下文菜单提供了新的数据库差异窗口。 它具有更好的 UI，并且清楚显示了执行同步后您将获得的结果。</span></span></p> 
           <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-26f0ee8bf5dfe9bb253e1569410c8bc22fb.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
           <p style="margin-left:0px; margin-right:0px"><span style="color:#19191c"><span style="background-color:#ffffff">图例显示了颜色对潜在结果的含义：</span></span></p> 
           <ul> 
            <li><span style="color:#19191c"><span style="background-color:#ffffff"><em>绿色和斜体：</em>将创建对象。</span></span></li> 
            <li><span style="color:#19191c"><span style="background-color:#ffffff"><em>灰色：</em>对象将被删除。</span></span></li> 
            <li><span style="color:#19191c"><span style="background-color:#ffffff"><em>蓝色：</em>对象将被更改。</span></span></li> 
           </ul> 
           <p style="color:rgba(25, 25, 28, 0.7); margin-left:0px; margin-right:0px; text-align:start"><span style="color:#19191c"><em>Script preview</em>（脚本预览）选项卡显示结果脚本，可在新控制台中打开或从此对话框运行。 此脚本应用更改后使右侧数据库（目标）成为左侧数据库（源）的副本。</span></p> 
           <p style="color:rgba(25, 25, 28, 0.7); margin-left:0px; margin-right:0px; text-align:start"><span style="color:#19191c">除了 Script preview（脚本预览）选项卡，数据库差异窗口底部窗格中还有两个选项卡：<em>Object Properties Diff</em>（对象属性差异）和 <em>DDL Diff</em>（DDL 差异）。 它们显示源数据库和目标数据库中对象的特定版本之间的差异。</span></p> 
           <h3><span style="color:#19191c"><span style="background-color:#ffffff">数据编辑器聚合</span></span></h3> 
           <div> 
            <p style="margin-left:0; margin-right:0"><span style="color:#19191c"><span style="background-color:#ffffff">可以显示一系列单元格的聚合视图。这是一项期待已久的功能，可帮助你管理数据而不必编写额外的查询！这使得数据编辑器更强大且更易于使用，使其更接近 Excel 和 Google 电子表格。</span></span></p> 
            <p style="margin-left:0px; margin-right:0px"><span style="color:#19191c"><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-ac3599b8b74976acc58054e51d6e4a1b731.png" width="700" referrerpolicy="no-referrer"></span></p> 
            <p style="margin-left:0px; margin-right:0px"><span style="color:#19191c"><span style="background-color:#ffffff"> 要使用此功能，首先选择要查看视图的单元范围，然后</span><em>点击鼠标右键</em><span style="background-color:#ffffff">并从菜单中选择 </span><em>Show Aggregate View</em><span style="background-color:#ffffff">（显示聚合视图）。</span></span></p> 
            <h3><span style="color:#19191c"><span style="background-color:#ffffff">进一步改进：</span></span></h3> 
            <div> 
             <ul> 
              <li><span style="color:#19191c"><span style="background-color:#ffffff">打开或导入 CSV 文件时，</span><span style="background-color:#ffffff">PyCharm 会自动检测第一行是否为标题以及是否包含列名称。</span></span></li> 
             </ul> 
             <p><span style="color:#19191c"><span style="background-color:#ffffff">更新公告：</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fwhatsnew%2F" target="_blank">https://www.jetbrains.com/pycharm/whatsnew/</a></p> 
            </div> 
           </div> 
          </div> 
         </div> 
        </div> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            