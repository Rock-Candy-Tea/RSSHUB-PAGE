
---
title: '.NET 7 预览版 2 已发布，增强 RegEx 源生成器、SDK 改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2858'
author: 开源中国
comments: false
date: Fri, 18 Mar 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2858'
---

<div>   
<div class="content">
                                                                                            <p> .NET 7 Preview 2 <span style="color:#333333">已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-2%2F" target="_blank">发布</a>，第二个预览版包括对 RegEx 源生成器的增强、将 NativeAOT 从实验状态转移到运行时的进展，以及对“dotnet new”CLI SDK 的一系列重大改进。</span></p> 
<p><span style="color:#333333">在此</span>下载适用于 Windows、macOS 和 Linux 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F7.0" target="_blank">.NET 7 Preview 2 。</a></p> 
<h3>引入新的正则表达式源生成器</h3> 
<p> 新的正则表达式源生成器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues" target="_blank">Issues</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F44676" target="_blank"> 44676</a>）在不增加启动成本的情况下，为编译带来了性能好处，还提供了良好的调试体验。</p> 
<p>要开始使用新的正则表达式源生成器，只需将包含类型转换为分部（<span style="color:#cc0000"><code>partial</code></span>）类型，并使用 <code>RegexGenerator</code> 属性声明一个新的分部方法。该方法将返回优化的 Regex 对象，源生成器将自动填充该方法的实现，并在更改模式或传递其他选项时自动更新。下面是一个例子：</p> 
<p><strong>之前：</strong></p> 
<pre><code class="language-cpp">public class Foo
&#123;
  public Regex regex = new Regex(@"abc|def", RegexOptions.IgnoreCase);

  public bool Bar(string input)
  &#123;
    bool isMatch = regex.IsMatch(input);
    // ..
  &#125;
&#125;</code></pre> 
<p><strong>现在：</strong></p> 
<pre><code class="language-cpp">public partial class Foo  // <-- Make the class a partial class
&#123;
  [RegexGenerator(@"abc|def", RegexOptions.IgnoreCase)] // <-- Add the RegexGenerator attribute and pass in your pattern and options
  public static partial Regex MyRegex(); //  <-- Declare the partial method, which will be implemented by the source generator

  public bool Bar(string input)
  &#123;
    bool isMatch = MyRegex().IsMatch(input); // <-- Use the generated engine by invoking the partial method.
    // ..
  &#125;
&#125;</code></pre> 
<h3>NativeAOT 更新</h3> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>该版本将 NativeAOT 从实验性的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntimelab" target="_blank">dotnet/runtimelab 存储库</a>中移出并进入稳定的运行时库 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime" target="_blank">dotnet/runtime</a> repo，</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>但尚未在 dotnet SDK 中添加足够的支持，以使用 NativeAOT 发布项目。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2>SDK 改进</h2> 
<ul> 
 <li> <h3><strong>新的 CLI 解析器 + 选项卡完成</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Ftemplating%2Fissues%2F2191" target="_blank"><strong>  #2191</strong></a><strong> </strong></h3> </li> 
</ul> 
<p><span style="color:#2e3033">.NET 新命令为许多子命令提供了更加一致和直观的界面，更新了大量对模板选项和参数的 TAB 补全的支持，在用户输入有效参数和选项时提供快速反馈。</span><span style="color:#333333">以下是新的帮助输出示例：</span></p> 
<pre><code class="language-cpp">❯ dotnet new --help
Description:
  Template Instantiation Commands for .NET CLI.

Usage:
  dotnet new [<template-short-name> [<template-args>...]] [options]
  dotnet new [command] [options]

Arguments:
  <template-short-name>  A short name of the template to create.
  <template-args>        Template specific options to use.

Options:
  -?, -h, --help  Show command line help.

Commands:
  install <package>       Installs a template package.
  uninstall <package>     Uninstalls a template package.
  update                  Checks the currently installed template packages for update, and install the updates.
  search <template-name>  Searches for the templates on NuGet.org.
  list <template-name>    Lists templates containing the specified template name. If no name is specified, lists all templates.</code></pre> 
<h3><span style="background-color:#ffffff; color:#2e3033">新命令名称</span></h3> 
<p><span style="background-color:#ffffff; color:#2e3033">帮助输出中的所有命令不再具有 -- 前缀，更符合用户对 CLI 应用程序中子命令的期望。 旧版本（--install 等）仍可用于防止破坏用户脚本，将来会在这些命令中添加过时警告以鼓励迁移。</span></p> 
<h3>Tab 补全</h3> 
<p>dotnet CLI 在 PowerShell、bash、zsh 和 fish 等流行的 shell 上支持 tab 补全已经有一段时间。 然而，实现有意义的补全取决于单独的 dotnet 命令。 对于 .NET 7，新命令学习了如何提供 Tab 补全：</p> 
<ul> 
 <li>可用的模板名称（在 dotnet new <template-short-name> 中）</li> 
</ul> 
<pre><code class="language-cpp">❯ dotnet new angular
angular              grpc                 razor                viewstart            worker               -h
blazorserver         mstest               razorclasslib        web                  wpf                  /?
blazorwasm           mvc                  razorcomponent       webapi               wpfcustomcontrollib  /h
classlib             nugetconfig          react                webapp               wpflib               install
console              nunit                reactredux           webconfig            wpfusercontrollib    list
editorconfig         nunit-test           sln                  winforms             xunit                search
gitignore            page                 tool-manifest        winformscontrollib   --help               uninstall
globaljson           proto                viewimports          winformslib          -?                   update</code></pre> 
<ul> 
 <li>模板选项（Web 模板中的模板选项列表）</li> 
</ul> 
<pre><code class="language-cpp">dotnet new web --dry-run
--dry-run                  --language                 --output                   -lang
--exclude-launch-settings  --name                     --type                     -n
--force                    --no-https                 -?                         -o
--framework                --no-restore               -f                         /?
--help                     --no-update-check          -h                         /h</code></pre> 
<ul> 
 <li>模板选项的允许值（选择模板参数上的选择值）</li> 
</ul> 
<pre><code class="language-cpp">dotnet new blazorserver --auth Individual
Individual     IndividualB2C  MultiOrg       None           SingleOrg      Windows</code></pre> 
<p> </p> 
<p>该预览版本还有大量其他更新项目，详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-2%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            