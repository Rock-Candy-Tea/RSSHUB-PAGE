
---
title: 'OpenSearch 2.0 发布，ElasticSearch 替代品性能大幅提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202206/04060804_RyWe.gif'
author: 开源中国
comments: false
date: Sat, 04 Jun 2022 06:08:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202206/04060804_RyWe.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">OpenSearch 2.0 现已正式发布！此版本融合了来自整个 OpenSearch 社区的用户反馈和贡献，以提供大量新功能和性能增强。我们非常感谢社区为构建分布式搜索和分析工具集而做出的协作努力，这些工具集具有开发人员可以依赖的功能，可用性和开源灵活性，以创建他们最具创新性的解决方案。</p> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">下面介绍了一些可以使用 OpenSearch 2.0 的新功能和增强功能。您可以在此处找到完整的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch-build%2Fblob%2Fmain%2Frelease-notes%2Fopensearch-release-notes-2.0.0.md" target="_blank">发行说明</a>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>Lucene 9.1</strong></h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">在2.0版本中，OpenSearch已升级到Lucene 9.1（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flucene.apache.org%2Fcore%2F9_1_0%2Findex.html" target="_blank">Lucene 9.1文档</a>）。迁移到最新版本的Lucene为这个版本提供了许多令人兴奋的进步，并将在未来的版本中继续提供更多的价值。对于 2.0，此升级启用了以下增强功能：</p> 
<ul> 
 <li>Lucene 9.1 提供<strong>的性能优化</strong>包括将多维点的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flucene.apache.org%2Fcore%2Fcorenews.html%23apache-lucenetm-900-available" target="_blank">索引速度提高了 10–15%</a>。</li> 
 <li><strong>Java Jigsaw模块支持  </strong>意味着在 9.1 版本中，Lucene 具有模块描述符和依赖项信息。这与OpenSearch的持续发展相一致，使工具集更加模块化和可扩展。</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>文档级警报</strong></h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start"><strong>文档级警报</strong>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Falerting%2Fissues%2F238" target="_blank">请参阅 GitHub 问题</a>）允许用户创建可按文档生成警报的监视器。这些监视器通常用于安全检测，其使用的方法与 OpenSearch 中提供的其他类型的警报监视器类似：查询级别和存储桶级别。虽然这些警报使用数据的汇总视图，但文档级警报可以对索引中的每个文档发出警报，突出显示哪些特定文档或记录正在触发监视器中的警报，并避免基于时间戳的监视间隙或数据重叠。</p> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start"><img alt="图像：文档级警报" src="https://static.oschina.net/uploads/img/202206/04060804_RyWe.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>通知</strong></h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">新的<strong>通知插件</strong>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fnotifications%2Fissues%2F181" target="_blank">参见GitHub问题</a>）为OpenSearch添加了一个统一的通知系统。用户不再需要独立配置和管理每个插件的通知通道;在2.0版本中，通知插件提供了一个集中的位置来设置和管理相关OpenSearch插件的通知。例如，除了管理警报插件的通知外，此插件还可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fdocs%2Flatest%2Fim-plugin%2Fism%2Findex%2F" target="_blank">索引状态管理</a><span> </span>（ISM） 插件中完成计划操作时生成通知。</p> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start"><img alt="图片：通知插件" src="https://static.oschina.net/uploads/img/202206/04060805_i9El.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>ML 共享资源升级</strong></h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">随版本 1.3 引入的<span> </span><strong>ML Commons 插件</strong>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fml-commons" target="_blank">请参阅 GitHub 存储库</a>在 2.0 版中获得了两个新算法，可将 OpenSearch 的机器学习 （ML） 功能扩展到其他工作负载，减少构建 ML 功能所需的工作量，并集中计算、资源管理和 ML 流程的安全性。用于线性回归和定位的新算法与 kmeans 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fblog%2Fodfe-updates%2F2019%2F11%2Frandom-cut-forests%2F" target="_blank">随机切割森林</a>的现有算法相结合，为构建和训练 ML 模型提供了全面的基础。线性回归的添加旨在简化用于预测分析的ML模型的开发;通过本地化，用户可以在开发 ML 方法方面抢占先机，这些方法可以揭示异常或检测到的任何事件的关键因素，从而促进根本原因分析和其他用例的分析和可视化。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">替换非包容性术语</h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">此版本将整个 OpenSearch 中的非包容性术语（如主、黑名单）替换为包容性术语（如集群管理器、白名单）。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2FOpenSearch%2Fissues%2F2589" target="_blank">请参阅 GitHub 中的问题</a>）。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">RPM 包管理器</h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">版本 2.0 遵循版本 1.3.2，以包括<span> </span><strong>RPM 包管理器</strong>分发版的可用性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch-build%2Fissues%2F27" target="_blank">请参阅 GitHub 问题</a>）。这简化了基于红帽 Linux 的操作系统的 OpenSearch 发行版的安装。您可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fdocs%2Flatest%2Fopensearch%2Finstall%2Fcompatibility%2F" target="_blank">在此处</a>查看兼容的 Linux 版本。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">重大更改和持续支持</h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">OpenSearch遵循语义版本控制或<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsemver.org%2F" target="_blank">SemVer</a>，因此重大更改仅包含在主要版本版本中，例如此版本。对于2.0版本，不兼容更改的列表包括上面提到的Lucene升级和包容性术语等更新，以及由于添加通知插件而在目标API中的重大更改以及其他更改。有关 2.0 版中重大更改的完整列表，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2FOpenSearch%2Fissues%2F2480" target="_blank">文档</a>。</p> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">请注意，我们将继续支持 OpenSearch 1.x 发行版。有关弃用支持的详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Ffaq%23q3.28" target="_blank">常见问题解答的第 3.28 节</a>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">为项目做贡献</h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">您的想法和贡献对 OpenSearch 项目产生了真正的影响！从Lucene升级到新插件再到ML进步，此版本包括来自OpenSearch社区的许多有价值的贡献。我们向所有为OpenSearch 2.0做出贡献的人致以最深切的感谢。</p> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">如果您有兴趣了解更多信息，有具体问题，或者只是想提供反馈，请访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2F" target="_blank">OpenSearch.org</a>，在 GitHub 上为<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2FOpenSearch%2Fissues" target="_blank">OpenSearch</a><span> </span>或<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2FOpenSearch-Dashboards%2Fissues" target="_blank">OpenSearch Dashboards</a><span> </span>打开问题，或在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.opensearch.org%2F" target="_blank">论坛</a>中发帖。还有定期<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.meetup.com%2FOpenSearch%2F" target="_blank">的社区会议</a>，包括每次会议的更新和问答时间。</p> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">对于几乎任何类型的贡献，打开问题是第一步。如果您渴望加入，请查看带有“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fissues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2Buser%253Aopensearch-project%2Blabel%253A%2522help%2Bwanted%2522" target="_blank">需要帮助</a>”标签的问题。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>立即开始</strong></h3> 
<p style="color:#002a3a; margin-left:0; margin-right:0; text-align:start">你可以在这里下载<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fversions%2Fopensearch-2-0-0.html" target="_blank">OpenSearch 2.0</a>！请务必在开始时查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch-build%2Fblob%2Fmain%2Frelease-notes%2Fopensearch-release-notes-2.0.0.md" target="_blank">发行说明</a>和更新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensearch.org%2Fdocs%2F2.0%2F" target="_blank">的文档</a>。</p>
                                        </div>
                                      
</div>
            