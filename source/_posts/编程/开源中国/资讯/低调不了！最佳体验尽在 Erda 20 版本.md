
---
title: '低调不了！最佳体验尽在 Erda 2.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/40aec4eba0084db0871dd0e9912d9add.gif'
author: 开源中国
comments: false
date: Wed, 16 Mar 2022 09:44:00 GMT
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/40aec4eba0084db0871dd0e9912d9add.gif'
---

<div>   
<div class="content">
                                                                                            <p>大家期待已久的 Erda V2.0 带着全新界面风格和特性改进震撼发布！</p> 
<p>本次版本升级也意味着 Erda 在技术层面不断提升的同时，在用户体验上也投入了大量精力。界面作为人机交互的重要“桥梁”，我们希望用户感受到的不仅仅是 Erda 的强大功能，更希望给大家呈现优雅、舒适的操作体验！那么下面我们一起来看看本次新版本将会有哪些亮点和大家见面～</p> 
<h1>亮点一：界面全新升级</h1> 
<h2>设计师有话说</h2> 
<p>Erda V2.0 是以黑白灰为基调，无论从情绪表达还是色彩搭配性上，这样的选择都更符合我们的要求。</p> 
<p><em><strong>“好的设计不是喧闹，而是换位思考”</strong></em></p> 
<h2>更纯粹</h2> 
<p>黑白灰作为极简主义的基本符号之一，剥除了很多主观意识，呈现出事物本质，折射最核心、最朴质内涵，让我们更热忱于对产品本身的探索。企业级产品，功能及内容是最优先的，杂乱的颜色会增加用户疲劳感，而黑白灰削弱了杂色，使内容突出，避免颜色分散使用者的注意力。其次黑白灰拥有最纯粹的美，它能瞬间带你进入静谧的世界，沉下心更好地去思考和工作。</p> 
<h2>更包容</h2> 
<p>不论是业务复杂性还是字段类型多样性，Erda 都“面面俱到”，那么就需要我们在视觉基调的选择上，具备足够的包容性。嘉柏丽尔·香奈儿说过：“黑色包容一切，白色亦然。它们的美无懈可击，完美和谐。”</p> 
<p>黑白灰作为调和色，能极大地降低各类状态、类型 tag 所带来的的视觉干扰，从而达到纯粹与层次的平衡，使宁静与高冷中带着阳光与温度。</p> 
<h1>亮点二：技术优化升级</h1> 
<p>全新视觉交互上新的同时，本次版本还重点推出了全新的项目级研发流程，在单应用 CI/CD 基础上，提供了项目级流水线、制品、环境管理的核心功能，真正意义上解决项目级的持续交付的难题。</p> 
<p><img alt="技术优化升级.gif" src="https://ucc.alicdn.com/pic/developer-ecology/40aec4eba0084db0871dd0e9912d9add.gif" referrerpolicy="no-referrer"></p> 
<h2>项目级流水线</h2> 
<p>在原来的单应用流水线管理的基础上进行了项目级的全局管理（原有应用下的流水线功能还保留），让开发者在需要管理执行多个应用的场景下，在项目级流水线中可以一次性的批量操作管理，无需不断切换应用进行管理，如用户只有单个应用或者只关注单应用的情况下，还是可以继续按原来的习惯，使用应用下的流水线进行管理和执行。</p> 
<p><img alt="image.png" src="https://ucc.alicdn.com/pic/developer-ecology/34ff9eb37bb64fceb57229074019316b.png" referrerpolicy="no-referrer"> 项目级流水线管理</p> 
<p><img alt="image.png" src="https://ucc.alicdn.com/pic/developer-ecology/41b786db6b7445b387c64d7dc0810aa7.png" referrerpolicy="no-referrer"> 应用流水线管理</p> 
<h2>项目制品管理</h2> 
<p>制品分为应用制品和项目制品，应用制品指部署一个应用所需的全部内容，包括镜像、依赖的 Addon 以及各类配置信息，通过制品可以直接在对应的当前环境或跨平台环境中进行安装部署，应用制品是由流水线中 release action 生成。</p> 
<p><img alt="image.png" src="https://ucc.alicdn.com/pic/developer-ecology/67479c18ec1a47ef8d64d66239f7edd6.png" referrerpolicy="no-referrer"> 应用制品</p> 
<p>项目制品由一个或多个应用制品按照一定部署顺序组成的制品。部署项目制品时，平台将根据您定义的部署顺序，分批部署该制品中引用的应用制品，项目制品通过测试后，可以手动转为正式制品交付实施团队进行升级交付。</p> 
<p><img alt="应用制品.gif" src="https://ucc.alicdn.com/pic/developer-ecology/8257f520a8b846ddb613bd821cd247b4.gif" referrerpolicy="no-referrer"></p> 
<h2>环境管理</h2> 
<p>在环境中，用户可以整体查看项目所有应用的 runtime 状态信息，对于自己应用依赖的应用是否存在即健康，可以清晰的感知，避免单应用部署过程中出错后调查发现依赖应用问题引起的，打破中间的信息差。在部署中心部署的方式有两种，一种是通过流水线自动部署，另外一种就是手动创建部署单进行部署管理（本次新增特性），具体步骤如下：</p> 
<ul> 
 <li><strong>配置部署参数</strong></li> 
</ul> 
<p><img alt="配置部署参数.gif" src="https://ucc.alicdn.com/pic/developer-ecology/f9989c18d8314812b8ca45b55b5eb89d.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>创建部署单，选择对应的项目制品</strong></li> 
</ul> 
<p><img alt="创建部署单，选择对应的项目制品.gif" src="https://ucc.alicdn.com/pic/developer-ecology/97a0482b77f14a33b630ce4192619871.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>执行部署单进行部署</strong></li> 
</ul> 
<h2>全新的服务可观测特性发布</h2> 
<p>在 1.5 版本中，发布了全新的微服务拓扑图功能，本次在拓扑中单个服务的下钻分析进行完善，具体包含单个服务总览、调用监控、链路查询和资源监控的内容，让单点问题的调查分析更简单清晰。</p> 
<p><img alt="全新的服务可观测特性发布.gif" src="https://ucc.alicdn.com/pic/developer-ecology/31d6cc3c1db148a49a4e4558f2f46021.gif" referrerpolicy="no-referrer"></p> 
<h2>个人工作台</h2> 
<p>本次的企业版中发布了个人工作台，个人在组织中的工作事和消息信息进行了汇聚，让用户更清晰便捷查看工作内容的同时，能够通过快捷入口快速直达到工作页面。</p> 
<p><img alt="image.png" src="https://ucc.alicdn.com/pic/developer-ecology/70390f4a3ac749fb982c3b4707e37acb.png" referrerpolicy="no-referrer"></p> 
<p>以上就是 Erda 2.0 全新版本的部分亮点及全新特性介绍，欢迎大家体验使用，非常期待大家的意见和建议～也再次感谢为本次改版辛苦付出的小伙伴们，希望我们的产品可以给大家带来更便捷、更高效的体验，这是我们技术人淳朴的心愿😊。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda%2Freleases" target="_blank">点击直达 Erda V2.0 Changelog</a></p> 
<p><strong>更多技术干货及精彩内容，尽请关注【尔达Erda】公众号～</strong></p>
                                        </div>
                                      
</div>
            