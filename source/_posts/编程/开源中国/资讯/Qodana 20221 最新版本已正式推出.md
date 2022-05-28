
---
title: 'Qodana 2022.1 最新版本已正式推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/657758bb-96ee-4f29-8c8f-49e98ac8e36b.png'
author: 开源中国
comments: false
date: Sat, 28 May 2022 07:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/657758bb-96ee-4f29-8c8f-49e98ac8e36b.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>快速概览：我们在持续添加新功能并改进我们的代码质量平台 Qodana。<strong>许可证审核</strong>此前一直是必须与主要 linter 分开配置的额外 linter，它现在随 Qodana 开箱即用。 我们还为 PHP 和 JVM linter 添加了许多<strong>新的实用检查</strong>。 现在就来了解一下吧！</p> 
 <p><img src="https://oscimg.oschina.net/oscnet/657758bb-96ee-4f29-8c8f-49e98ac8e36b.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0"><strong>许可证审核</strong></p> 
 <p style="margin-left:0; margin-right:0">如果代码中的许可证无效或使用不当，可能会导致非常昂贵的法律与合规处罚。 使用 Qodana，您可以扫描代码仓库中的依赖项，查找其许可证并查看是否存在潜在问题。</p> 
 <p><img height="308" src="https://oscimg.oschina.net/oscnet/3e42b6cb-63dc-4729-9a03-0364727fe9da.gif" width="578" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0">在此版本中，您可以轻松地将许可证审核引入项目并使之融入 CI/CD 管道。 新的<em>许可证审核</em>功能适用于所有 linter，包括 Python、Java、Kotlin、PHP 和 JavaScript。</p> 
 <p style="margin-left:0; margin-right:0">要启用<em>许可证审核</em>，应将以下行添加到项目根目录下的<code>qodana.yaml</code>文件中：</p> 
 <pre style="margin-left:0; margin-right:0"><code><strong style="color:#990000">include:</strong>
  - name: CheckDependencyLicenses</code></pre> 
 <p style="margin-left:0; margin-right:0">如果您需要忽略项目中的特定依赖项，请添加以下行：</p> 
 <pre style="margin-left:0; margin-right:0"><code><strong style="color:#990000">dependencyIgnores:</strong>
- name: <span style="color:#dd1144">"dependency/name"</span></code></pre> 
 <p style="margin-left:0; margin-right:0">我们的文档1提供了有关许可证审核自定义配置的更多信息，这篇博文2介绍了它将如何简化开发者、经理和法务团队的日常工作。</p> 
 <p style="margin-left:0; margin-right:0"><strong>PHP 检查</strong></p> 
 <p style="margin-left:0; margin-right:0">此版本的 Qodana 提供了 PhpStorm 2022.1 中的所有新检查，并通过我们的 PHP linter 将它们添加到您的管道中。PhpStorm 与 Qodana 捆绑，因此当 Qodana 提示代码问题时，您可以直接在 IDE 中将其打开进行进一步调查。</p> 
 <p><img src="https://oscimg.oschina.net/oscnet/c81b306a-64f3-4811-9cfb-4b954c728d2f.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>重复的数组键</strong></span></p> 
 <p style="margin-left:0; margin-right:0">在 PHP 中，<code>array_merge()</code>的行为不同于<code>+</code>运算符合并。 如果键重复，后者不会覆盖值。 这可能导致混乱和错误，因此 Qodana for PHP 现在会高亮显示此类情况。</p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>count($array) 的数组索引用法</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>将条目附加到数组时，无需显式指定索引。Qodana for PHP 将针对冗余的</span><code>count()</code><span>调用向您发出警告。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>将 pow()</strong></span><span style="color:transparent"><strong> 调用替换为 **</strong></span></p> 
 <p style="margin-left:0; margin-right:0">PHP 从 5.6 版开始提供<code>**</code>幂运算符。Qodana for PHP 将建议在 PhpStorm 中进行快速修复 (Alt+Enter)，使用 ** 运算符替换旧的<code>pow()</code>调用。</p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>只读属性</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>可以使用</span><code>readonly</code><span>标志声明在类中具有只读访问权限的 private 属性。Qodana for PHP 将建议更新属性声明。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>final 类常量</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000">从 PHP 8.1</span> 开始，可以将常量声明为 final。 这就是为什么 Qodana for PHP 会针对未继承的常量向您发出警告并建议向其<span style="color:#000000">添加<code>final</code>修饰符。 通过 PhpStorm 集成，您可以快速跳转到 IDE 来修正问题。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>反向顺序的 r</strong></span><span style="color:transparent"><strong>and 函数实参</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>此检查会高亮显示来自 rand 系列的函数调用，其中 max 实参可能小于 min。 例如，调用</span><code>rand(10, 1)</code><span>与调用</span><code>rand(1, <span style="color:#000000">10)</span></code><span style="color:#000000">相同，但<code>mt_rand()</code>对其实参顺序的要求非常严格。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>PHPUnit 的</strong></span><span style="color:transparent"><strong>无效模拟目标</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>尝试访问模拟对象上的 private 或 final 方法时，Qodana for PHP 会向您发出警告。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>冗余</strong></span><span style="color:transparent"><strong>修饰符</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>此新检查将报告在正则表达式模式中使用但不影响匹配的修饰符：</span></p> 
 <ul style="list-style-type:disc"> 
  <li> <p>不包含字母的模式中的<code>/i</code>（不区分大小写）。</p> </li> 
  <li> <p>不包含美元符号或包含<code>\m</code>(PCRE_MULTILINE) 修饰符的模式中的<code>/D</code>(PCRE_DOLLAR_ENDONLY)。</p> </li> 
  <li> <p>不包含点的模式中的<code>/s</code>（点匹配换行符）。</p> </li> 
 </ul> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>不支持的修饰符</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>此检查将报告</span><code>/e</code><span>修饰符（在 PHP 7.0 及更高版本中被弃用）的用法。</span></p> 
 <p style="margin-left:0; margin-right:0"><strong>Java 和 Kotlin 检查</strong></p> 
 <p style="margin-left:0; margin-right:0">此版本还将<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkwNDI5NzUyMQ%3D%3D%26mid%3D2247488234%26idx%3D1%26sn%3Df088cda202275b988d5f74b3574469df%26chksm%3Dc0887fb4f7fff6a2208a3b3743e245f93a851e88eebe9f630255d7e73a0bb2c5ab6fbe958ed1%26scene%3D21%23wechat_redirect" target="_blank"> IntelliJ IDEA 2022.1 </a>中的新检查添加到 Qodana for JVM。 借助我们的 IntelliJ IDEA 集成，发现问题后可以直接在 IDE 中打开错误代码进行快速修复。</p> 
 <p><img src="https://oscimg.oschina.net/oscnet/f1ebdde7-834b-46cf-8216-26baa4ef2525.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0">以下是最值得注意的检查。</p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>可疑的</strong></span><span style="color:transparent"><strong>反向引用</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>Qodana for JVM 将找到在运行时无法解析的引用。这意味着反向引用永远不会匹配任何内容。 如果组是在反向引用之<span style="color:#000000">后定义的，或者组是在交替的不同分支中定义的，则反向引用将无法解析。</span></span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>可以使用 ‘Files’ 方法构建</strong></span><span style="color:#000000"><strong> ‘Inpu</strong></span><span style="color:transparent"><strong>tStream’ 和 ‘OutputStream’</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>当</span><code>FileInputStream</code><span>和</span><code>FileOutputStream</code><span>构造函数可以分别被替换为</span><code>Files.newInputStream()</code><span>和</span><code>Files.newOutputStream()</code><span>时，此检查会报告。 使用</span><code>Files</code><span>方法创建的流通常比使用流构造函数创建的流更有效。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>可以使用批量 ‘Files.readAttributes’ </strong></span><span style="color:#000000"><strong>调用替换多个文件特性调用</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span>此检查会查找连续使用多个 java.io.File 特性检查（例如</span><code>isDirectory</code><span>、</span><code>isFile</code><span>、</span><code>lastModified</code><span>或</span><code>length</code><span>）的位置。 这些调用可被替换为批量<code><code>Files.readAttributes</code></code>调用。 批量方法通常比多个特性检查更高效。     </span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>循环可以替换为 ‘List.replaceAll()’</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000">此检查报告可以折叠成单个<code>List.replaceAll()</code>调用的循环。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>占位符数量与日志记录调用</strong></span><span style="color:#000000"><strong>中的实参数量不匹配</strong></span></p> 
 <p style="margin-left:0; margin-right:0">Qodana for JVM 将报告<code>SLF4J</code>或<code>Log4j 2</code>日志记录调用，例如<code>logger.info(\"&#123;&#125;: &#123;&#125;\", key)</code>，其中记录器消息中的<code>&#123;&#125;</code>占位符数量与日志记录调用中的其他实参数量不匹配。</p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong>正则表达式可以简化</strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000">此检查将检测可以简化的正则表达式</span>。</p> 
 <p style="margin-left:0; margin-right:0">要从分析中排除特定检查，您可以自定义默认检查配置文件或创建一个全新的配置文件。 您可能还希望执行对您的编码准则或最佳做法很重要的检查。 查看我们的 Qodana 文档3获取更多信息。</p> 
 <p style="margin-left:0; margin-right:0">以上就是 Qodana 2022.1 的所有最新变化。 我们希望这些博文对您有所帮助。<strong> 如果您想详细了解 Qodana 可以如何帮助您和您的业务，</strong>给我们留言，或发送电子邮件与我们联系。</p> 
 <ul style="list-style-type:disc"> 
  <li> <p style="margin-left:0; margin-right:0">中文销售支持：<span style="color:#337ab7">sales.cn@jetbrains.com</span></p> </li> 
  <li> <p style="margin-left:0; margin-right:0">中文技术支持：<span style="color:#337ab7">support.cn@jetbrains.com</span></p> </li> 
 </ul> 
 <p style="margin-left:0; margin-right:0"><strong>参考链接</strong></p> 
 <ol style="list-style-type:decimal"> 
  <li> <p style="margin-left:0; margin-right:0">我们的文档：</p> <p style="margin-left:0; margin-right:0"><span style="color:#337ab7">https://www.jetbrains.com/help/qodana/license-audit.html</span></p> </li> 
  <li> <p style="margin-left:0; margin-right:0">这篇博文：</p> <p style="margin-left:0; margin-right:0"><span style="color:#337ab7">https://blog.jetbrains.com/qodana/2022/05/keep-your-dependency-licenses-in-check/</span></p> </li> 
  <li> <p style="margin-left:0; margin-right:0">Qodana 文档：</p> <p style="margin-left:0; margin-right:0"><span style="color:#337ab7">https://www.jetbrains.com/help/qodana/qodana-yaml.html#Include+an+inspection+into+the+analysis+scope</span></p> </li> 
 </ol> 
 <p style="margin-left:0; margin-right:0"><strong>本博文英文原作者：Anastasia Khramushina</strong></p> 
 <p> </p> 
 <p><img src="https://oscimg.oschina.net/oscnet/b08b432e-90f8-4aa4-a3d3-f9b0b7b43e93.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0"><strong>关于 Qodana</strong></p> 
 <p style="margin-left:0; margin-right:0"><strong>Qodana 是一款代码质量监控平台，可用于评估您拥有、协作或购买的代码的完整性。它将您所喜爱的JetBrains IDE 中的所有智能功能以及诸如克隆检测和许可证审查等项目级检查引入到您的 CI/CD 管道中。</strong></p> 
</div>
                                        </div>
                                      
</div>
            