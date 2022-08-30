
---
title: '盛夏莫干山清凉发布 Zadig v1.14.0：工作流更自由、环境更强大'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ad2a5efb1e59c29e4c08699bea38ec11cde.png'
author: 开源中国
comments: false
date: Tue, 30 Aug 2022 00:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ad2a5efb1e59c29e4c08699bea38ec11cde.png'
---

<div>   
<div class="content">
                                                                                            <p>炎炎盛夏，全球变暖，一周年之际，Zadig 团队在浙西莫干山发版，正式推出 Zadig v1.14.0。</p> 
<p>经过一年的发展，Zadig 产品的完整性、易用性、扩展性上都得到了充分的发展，和社区小伙伴一起，茁壮成长。本次版本推出更为强大的自定义工作流，满足企业在交付链条上的流程编排需求，是在 Zadig 独有利剑“环境治理”能力之后又一重大功能，进一步帮助企业面向各种场景、高度自主地开发自定义模块和服务，同时拥抱更多合作伙伴和工程师可以参与进来，在整个云原生软件交付生命周期中编排任何有益迭代高质量产品的服务和价值。Enjoy ～</p> 
<h2>工作流无所不能，企业流程 100% 可适配</h2> 
<p>工作流触发机制更灵活，支持 Git 触发器、执行部分任务 <img alt src="https://oscimg.oschina.net/oscnet/up-ad2a5efb1e59c29e4c08699bea38ec11cde.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-8bd10c4f7a3486aa5fd3a1ef0925e086ebe.png" referrerpolicy="no-referrer"></p> 
<p>工作流策略设计更方便，支持配置默认分支 <img alt src="https://oscimg.oschina.net/oscnet/up-e5ffc5df8c1508024ab8c1c888475c5500a.png" referrerpolicy="no-referrer"></p> 
<p>丰富的变量能力，支持参数化配置工作流，在各阶段之间传递信息 <img alt src="https://oscimg.oschina.net/oscnet/up-174bf416fb7b33ccb9c8bed5ac8a56af9d4.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-1b4eb7a7abf52645f7afbf79f68d9a07dd9.png" referrerpolicy="no-referrer"></p> 
<p>开放的任务编排设计，企业可自定义开发适配自身业务流程的模块 <img alt src="https://oscimg.oschina.net/oscnet/up-5119a348821f8e7e097bcb53971ab92c7a6.png" referrerpolicy="no-referrer"></p> 
<h2>环境能力进一步增强，工程师体验更便利</h2> 
<p>支持基于已有 K8s YAML 环境复制，一键拉起指定版本的环境 <img alt src="https://oscimg.oschina.net/oscnet/up-e8a162b8a65f5d789bb2ecbe7b2a8d4e616.png" referrerpolicy="no-referrer"></p> 
<p>支持查阅环境变更记录，让操作有迹可循 <img alt src="https://oscimg.oschina.net/oscnet/up-f976e01fe58656edaf15efc2ea3b7a29027.png" referrerpolicy="no-referrer"></p> 
<p>支持下载容器中文件，debug 能力更上一层楼 <img alt src="https://oscimg.oschina.net/oscnet/up-5cb833f8b482e43f4ac729f67496a759de8.png" referrerpolicy="no-referrer"></p> 
<h2>系统架构更精简，集群接入很方便</h2> 
<p>系统架构缩减，降低维护和使用负担，详细信息可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkoderover%2Fzadig%2Fblob%2Fmain%2FSystem-Architecture-Overview.md" target="_blank">Zadig 系统架构</a> <img alt src="https://oscimg.oschina.net/oscnet/up-8246b91d07e6bd874b51bd2a55e6655a125.png" referrerpolicy="no-referrer"></p> 
<p>多集群管理支持 kubeconfig 方式，即使外接集群网络不能连通 Zadig 所在集群也可成功接入，从此不再受网络掣肘 <img alt src="https://oscimg.oschina.net/oscnet/up-68b96f70ababdc26fbcf1065448a03de0fb.png" referrerpolicy="no-referrer"></p> 
<h2>效能 API 全面开放，洞悉数据背后的价值</h2> 
<p>支持通过 OpenAPI 获取构建、部署、测试的效能数据，客观洞悉数据背后的价值 <img alt src="https://oscimg.oschina.net/oscnet/up-8c09bba14f536eb1a75abe78925b5389e47.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-e804fbbaf1ce305f04a73ecb34e792f6b33.png" referrerpolicy="no-referrer"></p> 
<h2>托管项目加协作模式，用 Zadig 上云原生</h2> 
<p>托管项目 0 负担接入 Zadig，通过协作模式批量分配工作流、环境的权限。先人一步，走上云原生交付之路。 <img alt src="https://oscimg.oschina.net/oscnet/up-896946b0be188b82b062b9078c7e8a98bd8.png" referrerpolicy="no-referrer"></p> 
<h2>新增功能详情列表</h2> 
<p><strong>工作流</strong></p> 
<ul> 
 <li>产品工作流支持配置默认分支</li> 
 <li>自定义工作流支持通用任务</li> 
 <li>自定义工作流支持选择部分任务执行</li> 
 <li>自定义工作流构建任务支持配置默认分支</li> 
 <li>自定义工作流支持使用自定义任务</li> 
 <li>自定义工作流支持全局变量</li> 
 <li>自定义工作流支持 Git 触发器</li> 
 <li>自定义工作流支持 MySQL 任务</li> 
 <li>支持在 Sonar 代码扫描中使用变量 $BRANCH 获取代码分支</li> 
</ul> 
<p><strong>环境</strong></p> 
<ul> 
 <li>Helm Chart 项目和 K8s YAML 项目更新环境前添加 dryRun 操作</li> 
 <li>环境支持变更记录</li> 
 <li>K8s YAML 项目支持环境复制</li> 
 <li>支持从容器中下载文件</li> 
</ul> 
<p><strong>其他</strong></p> 
<ul> 
 <li>托管项目支持协作模式</li> 
 <li>开发者中心开放效能洞察 API</li> 
 <li>多集群管理支持 kubeconfig 方式</li> 
 <li>Zadig 架构优化，合并组件</li> 
</ul> 
<p><strong>缺陷与优化</strong></p> 
<ul> 
 <li>修复托管项目中有同名服务时，工作流 Webhook 不生效问题</li> 
 <li>修复自定义工作流自定义构建镜像 PATH 被覆盖问题</li> 
 <li>修复自定义工作流构建任务无法拉取自定义构建镜像问题</li> 
 <li>修复自定义构建变量名称修改后变量值无效问题</li> 
 <li>修复交付物工作流中扩展步骤无效问题</li> 
 <li>修复代码扫描中克隆目录无效的问题</li> 
 <li>支持 IP + PORT 形式配置通用 Git 代码源</li> 
</ul> 
<h2>Release Note</h2> 
<p><strong>Workflow</strong></p> 
<ul> 
 <li>Workflows can choose their own default branches.</li> 
 <li>Implement general job for custom workflow.</li> 
 <li>Jobs can partially be executed in custom workflow.</li> 
 <li>Implement custom job for custom workflow.</li> 
 <li>Enable global variables for custom workflow.</li> 
 <li>Enable webhooks for custom workflow.</li> 
 <li>Implement Mysql plugin for custom workflow.</li> 
 <li>Enable the use of $BRANCH parameter in code scan.</li> 
</ul> 
<p><strong>Environment</strong></p> 
<ul> 
 <li>Dry run functionality for both helm chart project and yaml project.</li> 
 <li>Operation logs for environment changes</li> 
 <li>Environment duplication functionality for yaml project.</li> 
 <li>Download files from pods in environment pages.</li> 
</ul> 
<p><strong>Improvements & Bugfixes</strong></p> 
<ul> 
 <li>Collaboration mode has been enabled for loaded projects.</li> 
 <li>OpenAPI for build, test and deploy statistics.</li> 
 <li>Clusters can be managed by kubeconfigs instead of agents.</li> 
 <li>Merged some microservices.</li> 
 <li>Codehost with git protocol is now compatible with repository with IP + port.</li> 
 <li>Multiple code-scan improvements.</li> 
 <li>Multiple webhook bugfixes</li> 
 <li>Multiple workflow improvements.</li> 
</ul> 
<p>Zadig，让工程师更专注创造。欢迎加入 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg4NDY0NTMyNw%3D%3D%26mid%3D2247485614%26idx%3D2%26sn%3D408952415996c09a72c000f651ee1928%26chksm%3Dcfb4440ef8c3cd18c4d2a0be5db803422b22d9086d771645acc39727e863d98dfa60b5be596c%26scene%3D21%23wechat_redirect" target="_blank">开源吐槽群🔥</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fwww.oschina.net%252Faction%252FGoToLink%253Furl%253Dhttps%25253A%25252F%25252Fgithub.com%25252Fkoderover%25252Fzadig">Zadig on Github</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fgitee.com%252Fkoderover%252Fzadig">Zadig on Gitee</a></p>
                                        </div>
                                      
</div>
            