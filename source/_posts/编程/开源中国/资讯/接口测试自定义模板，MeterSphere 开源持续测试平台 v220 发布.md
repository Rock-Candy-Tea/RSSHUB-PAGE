
---
title: '接口测试自定义模板，MeterSphere 开源持续测试平台 v2.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b33ab5422edf0affd44c7411a7de74a5cd0.png'
author: 开源中国
comments: false
date: Mon, 26 Sep 2022 13:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b33ab5422edf0affd44c7411a7de74a5cd0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="670" src="https://oscimg.oschina.net/oscnet/up-b33ab5422edf0affd44c7411a7de74a5cd0.png" width="1362" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2022年9月26日，MeterSphere一站式开源持续测试平台正式发布v2.2.0版本。</p> 
<p style="margin-left:0; margin-right:0">在这一版本中，MeterSphere在<strong><span style="color:#783887">接口测试</span></strong>模块中，<span>接口定义支持自定义模板</span>，用户可以在模板中添加自定义字段，以满足不同研发团队在接口管理方面的个性化需求；在<span style="color:#783887"><strong>UI测试</strong></span>模块中，<span>支持自定义组合指令</span>，这一设计很好地将Robot Framework中的关键字封装技术落地到平台中，进一步提升了场景的可复用性以及可扩展性；在<span style="color:#783887"><strong>项目设置</strong></span>模块中，<span>文件管理支持对接第三方仓库（例如GitHub、GitLab和Gitee）</span>，用例与文件的关联变得更加简单，依托第三方仓库良好的版本管理机制，MeterSphere关联第三方仓库文件也支持多版本以及版本追溯。</p> 
<h2 style="margin-left:0; margin-right:0">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887"><strong>■ 接口测试支持自定义模板</strong></span></p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v2.2.0版本中，新增了接口模板，用于给接口定义添加自定义字段，以满足不同研发团队对接口定义的管理需求。</p> 
<p><img alt height="1470" src="https://oscimg.oschina.net/oscnet/up-19f105a8b57a16d24265175d4ff7621430d.png" width="2948" referrerpolicy="no-referrer"></p> 
<p>在自定义模板时，可以从系统已有的字段中添加，也支持设置新的自定义字段。如下图所示，在微服务架构中，因为服务众多，如何快速区分当前接口属于哪一个应用可以通过添加一个应用ID的字段来解决。</p> 
<p><img alt height="1464" src="https://oscimg.oschina.net/oscnet/up-9a8186b944d184a499e59df63bcfb799c25.png" width="2932" referrerpolicy="no-referrer"></p> 
<p>在项目设置中指定接口定义的模板后，创建新接口时就可以看到已经添加的自定义字段了。</p> 
<p><img alt height="1460" src="https://oscimg.oschina.net/oscnet/up-ba8d60b79ecfde8f96056ce90f66db8f3ea.png" width="2944" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#783887">■ UI测试支持自定义组合指令（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">MeterSphere的UI自动化测试支持自由场景编排和自由场景组合，实现了场景的高可复用性。</p> 
<p style="margin-left:0; margin-right:0">但在实际设计测试用例的过程中，我们会发现有很多测试步骤一直在重复添加。比如创建不同协议的用例，基础信息字段在每个协议的用例中都需要添加一遍。如果能把涉及基础信息字段的步骤组合成一个指令，那么在其他用例添加这些步骤时只需要添加这个指令即可。</p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v2.2.0版本中，我们从场景中扩展出了指令分类，用户可以将常用的测试步骤组合成新的自定义指令，在场景中添加使用。同时，MeterSphere也支持在场景中选中指定的步骤另存为自定义指令。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1462" src="https://oscimg.oschina.net/oscnet/up-faa086164214c7f7d9191ca73a2fbecd838.png" width="2950" referrerpolicy="no-referrer"></p> 
<p><img alt height="1462" src="https://oscimg.oschina.net/oscnet/up-9acbfe80e5b8e9b504cb7130502cb8168cc.png" width="2946" referrerpolicy="no-referrer"></p> 
<p><img alt height="1462" src="https://oscimg.oschina.net/oscnet/up-80f6d5dcc274417532a561b9eab9e8fc1b1.png" width="2948" referrerpolicy="no-referrer"></p> 
<p><span style="color:#783887"><strong>■ 文件管理支持对接第三方仓库（X-Pack增强包内）</strong></span></p> 
<p style="margin-left:0; margin-right:0">MeterSphere的文件管理功能用于存放用户需要使用的文件。在MeterSphere v2.1.0版本中，已经实现了本地上传的文件可以转存到文件管理中心，同时测试用例可以直接关联“文件管理”页面中的文件。</p> 
<p style="margin-left:0; margin-right:0">在MeterSphere v2.2.0中，我们进一步优化了文件管理功能，支持对接第三方仓库（例如GitHub、GitLab和Gitee）。测试用例可以直接在“文件管理”页面中选择第三方仓库的文件进行关联和使用，在这里也可以对第三方仓库的文件进行实时同步。</p> 
<p style="margin-left:0; margin-right:0">在“文件管理”页面中创建模块时，可以选择新建普通模块或存储库。录入存储库信息并测试连接通过后，指定文件所在分支以及文件路径，即可从第三方仓库拉取文件至MeterSphere平台。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1460" src="https://oscimg.oschina.net/oscnet/up-c66f6410791984b8be08aa55a7213532f4a.png" width="2950" referrerpolicy="no-referrer"></p> 
<p><img alt height="1460" src="https://oscimg.oschina.net/oscnet/up-7cc7335c2f3b445aebef290d4ab3699e5ee.png" width="2950" referrerpolicy="no-referrer"></p> 
<p>查看第三方仓库文件时，MeterSphere平台提供文件的基础信息、文件关联的用例，以及文件同步到平台的版本历史展示。</p> 
<p><img alt height="1456" src="https://oscimg.oschina.net/oscnet/up-1170ae03ca022eb27d560cb12ede6cfb21a.png" width="2946" referrerpolicy="no-referrer"></p> 
<p>更新文件时，可以批量或单独选择需要同步更新文件的相关用例，实现了同一个文件可以被不同用例关联不同文件版本的需求。</p> 
<p><img alt height="1178" src="https://oscimg.oschina.net/oscnet/up-afd567583028dabf93c1d635cc7c1b6dddd.png" width="1872" referrerpolicy="no-referrer"></p> 
<h2>功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>测试跟踪：测试计划/用例评审页用例标题展示优化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>接口测试：接口CASE高级搜索增加路径搜索；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>接口测试：TCP协议支持一键将XML文本格式转换为表格格式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>UI测试（X-Pack）：列表批量执行与测试计划执行时增加失败重试机制；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>UI测试（X-Pack）：测试报告支持一键分享；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>UI测试（X-Pack）：UI场景支持查看被引用列表；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>UI测试（X-Pack）：支持在配置文件中配置浏览器的默认分辨率；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>系统设置（X-Pack）：消息通知模板新增测试计划报告相关字段；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■<span> </span></span>通用功能（X-Pack）：版本筛选支持手动录入版本号。</p> 
<h2 style="margin-left:0; margin-right:0">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复在测试计划报告中点击名称链接会直接跳转到接口用例或者场景用例详情页的问题（GitHub #17993）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复“测试跟踪”首页未评审数量、覆盖数量与跳转后列表用例数量不一致的问题（GitHub #17910）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（测试跟踪）：修复项目自定义ID开启导入显示的是系统默认ID的问题（GitHub #17928）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复环境变量优先级大于场景变量的问题（GitHub #17873）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（接口测试）：修复接口自动化编辑场景并保存后，列表中“通过率”未更新的问题（GitHub #17784）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（UI测试）：修复UI自动化场景中导入了已有场景后，导致整个场景以及子场景的调试模式和测试计划不会被执行的问题（GitHub #17649）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887">■</span><span> </span>fix（UI测试）：修复测试计划中定时执行多个UI自动化场景，存在已执行失败的场景被标注为“未执行”的问题（GitHub #17649）。</p> 
<p style="margin-left:0; margin-right:0">除了上述提到的新增功能和优化外，MeterSphere v2.2.0版本还包含很多其他功能的更新和优化，欢迎进入MeterSphere项目的官方文档及GitHub仓库的Release页面，查看更加详细的更新日志。</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#783887"><strong>温馨提示：</strong></span>欢迎到MeterSphere专业测试云（ www.metersphere.com ）体验MeterSphere v2.2.0版本的新增功能。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="968" src="https://oscimg.oschina.net/oscnet/up-2124c4a8cd58cec2dee801569eb9f81ca2b.png" width="2950" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            