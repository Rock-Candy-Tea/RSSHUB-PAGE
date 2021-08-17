
---
title: 'DevUI Admin 2.0 重磅发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202108/17063604_XMsq.jpg'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 20:42:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202108/17063604_XMsq.jpg'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a>是面向企业中后台产品的开源前端解决方案，其设计价值观基于"至简"、"沉浸"、"灵活"三种自然与人文相结合的理念，旨在为设计师、前端开发者提供标准的设计体系，并满足各类落地场景，是一款企业级开箱即用的产品。如果你正在开发 ToB 的工具类产品，DevUI 将是一个很不错的选择！</p> 
<h1>引言</h1> 
<p>预告了2个星期，DevUI Admin 2.0 终于来了！先来看看<code>黑科技</code>是什么吧！</p> 
<p>在2.0版本中，我们将<code>区块</code>从<code>Admin</code>中抽离了出来，并且推出了一套对应的<code>Angular CLI</code>去帮助你使用我们的区块，让你可以更快更方便地搭建一个基于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank">DevUI Admin</a>的后台管理系统。后续我们还会持续丰富现有的区块，完善CLI让其能够帮助你做更多的事情。</p> 
<p>除此之外，我们还新增了：</p> 
<ul> 
 <li>动态表单</li> 
 <li>第三方登录，账号注册</li> 
 <li>消息提醒面板</li> 
</ul> 
<p>为了让大家快速将<code>黑科技</code>用起来，我们特意在B站录制了一段<code>4分钟</code>的教学视频，欢迎大家围观～</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1o3411z7qi%2F" target="_blank">https://www.bilibili.com/video/BV1o3411z7qi/</a></p> 
<h1>1 DevUI Admin 区块</h1> 
<p>目前<code>DevUI Admin</code>提供了<code>4类</code>共<code>19个</code>内置区块，覆盖<code>表单</code>、<code>列表</code>、<code>图表</code>等丰富的业务场景。</p> 
<p><img alt="materials-1.png" src="https://static.oschina.net/uploads/img/202108/17063604_XMsq.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt="materials-2.png" src="https://static.oschina.net/uploads/img/202108/17063604_ur55.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt="materials-3.png" src="https://static.oschina.net/uploads/img/202108/17063604_3cjo.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt="materials-4.png" src="https://static.oschina.net/uploads/img/202108/17063604_1T76.jpg" referrerpolicy="no-referrer"></p> 
<p>为了更方便的使用我们的区块，我们建议你先初始化我们的种子工程，再通过我们提供给你的 cli 来添加我们的区块以及基于我们的区块来搭建一个页面：</p> 
<pre><code>ng add ng-devui-admin
</code></pre> 
<p>初始化我们的种子工程之后，别忘了先安装我们的物料库哦：</p> 
<pre><code>npm i ng-devui-materials
</code></pre> 
<p>之后你就可以在你的项目中通过我们提供的命令行来进行区块的添加以及页面的创建：</p> 
<pre><code>ng g ng-devui-admin:blocks
ng g ng-devui-admin:views
</code></pre> 
<p>在这里你需要知道我们区块的名字，你可以前往 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-materials%2F" target="_blank">Admin 区块</a> 进行查看。</p> 
<h2>1.1 在页面中添加区块</h2> 
<pre><code># For Example
cd src/app/pages/getting-started/sample
ng g ng-devui-admin:blocks
</code></pre> 
<p>通过使用我们提供的 <code>ng-devui-admin</code> 命令行，通过简单的命令行操作你就可以将我们的区块快速添加到你的页面当中，之后你只需要简单的调整布局或者内容的调整就可以完成页面的搭建，布局的调整可以参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fdocs%2Flayout" target="_blank">Admin 布局</a>。</p> 
<p><img alt="block.gif" src="https://static.oschina.net/uploads/img/202108/17063604_rNXl.jpg" referrerpolicy="no-referrer"></p> 
<h2>1.2 基于区块创建页面</h2> 
<pre><code># For Example
cd src/app/pages/getting-started
ng g ng-devui-admin:views
</code></pre> 
<p>通过使用我们提供的 <code>ng-devui-admin</code> 命令行，通过简单的命令行操作你就可以初始化一个页面并添加我们提供的区块，再将其添加到对应的模块中，之后根据你的需要自行进行调整即可，更多使用可以参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fdocs%2Fgetting-started" target="_blank">DevUI Admin</a>。</p> 
<p><img alt="view.gif" src="https://static.oschina.net/uploads/img/202108/17063605_iFov.jpg" referrerpolicy="no-referrer"></p> 
<h1>2 动态表单</h1> 
<p>由于中后台应用表单需求较多，通过多次书写繁琐的表单模板进行表单创建，费时费力。DevUI Admin对DevUI组件库的表单组件进行了二次封装，你可以根据我们规定的对象模型元数据来动态的创建表单。另外，DevUI Admin已内置radio、checkbox、textInput、toggle、select等多个小部件可供选择，在表单内渲染。</p> 
<p><img alt="dynamic-forms.gif" src="https://static.oschina.net/uploads/img/202108/17063606_RZrL.jpg" referrerpolicy="no-referrer"></p> 
<p>更多使用细节请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fdocs%2Fdynamic-forms" target="_blank">Admin 动态表单</a>。</p> 
<h1>3 第三方登录</h1> 
<p>在Admin 2.0中我们提供了第三方登录的实现方式（示例为通过github登录），你可以拿到返回的 <code>code</code> 来进行你的用户鉴权等操作，更多细节参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fdocs%2Fauthority" target="_blank">第三方登录</a>。</p> 
<p><img alt="third-party.gif" src="https://static.oschina.net/uploads/img/202108/17063606_YNYs.jpg" referrerpolicy="no-referrer"></p> 
<h1>4 消息提醒面板</h1> 
<p>作为后台管理系统的使用者，时常会需要关注当前的消息以及有哪些待处理的事项，为了满足这一个需求，我们在 Admin 2.0 中已经实现了该功能。</p> 
<p><img alt="message.gif" src="https://static.oschina.net/uploads/img/202108/17063607_5lKe.jpg" referrerpolicy="no-referrer"></p> 
<h1>5 结语</h1> 
<p>在未来我们将持续演进，关注 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui-admin" target="_blank">DevUI Admin</a> 性能与易用性，持续优化 DevUI Admin 体验并降低开发者使用成本。期待你收到你的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui-admin%2Fissues" target="_blank">意见与建议</a>，同时也期待你的参与和共建。</p> 
<h1>6 DevUI 生态</h1> 
<h2>6.1 DevUIHelper：用于DevUI组件代码补全的VSCode插件</h2> 
<p>DevUIHelper 插件的开发旨在为组件库用户提供更优的开发体验，此外也是对VSCode插件开发的一次探索。</p> 
<p>代码库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2FDevUIHelper" target="_blank">https://github.com/DevCloudFE/DevUIHelper</a></p> 
<p>插件开发相关文章：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6844904202842406919" target="_blank">!好用到飞起！VSCode插件DevUIHelper设计开发全攻略（一）</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6856583300392681480" target="_blank">!好用到飞起！VSCode插件DevUIHelper设计开发全攻略（二）</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6856934676406370311" target="_blank">!好用到飞起！VSCode插件DevUIHelper设计开发全攻略（三）</a></p> 
<p>功能详情</p> 
<ol> 
 <li>为组件和指令提供了代码自动补全功能，自动补全必选参数，提供组件/指令支持的所有API信息进行选择的能力</li> 
</ol> 
<p><img alt="devui-helper.gif" src="https://static.oschina.net/uploads/img/202108/17063608_KnSL.jpg" referrerpolicy="no-referrer"></p> 
<ol start="2"> 
 <li>鼠标悬浮在组件标签和组件API上时，提供对应的提示信息，包括使用场景、API详情描述等关键内容</li> 
</ol> 
<p><img alt="devui-helper2.gif" src="https://static.oschina.net/uploads/img/202108/17063608_nk2H.jpg" referrerpolicy="no-referrer"></p> 
<h2>6.2 Vue DevUI：Vue3版本DevUI组件库</h2> 
<p><a href="https://gitee.com/devui/vue-devui">Vue DevUI</a>是<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a>团队为了响应社区声音、将DevUI的优秀实践覆盖更广泛的开发者而启动的一个Vue3版本的开源组件库，目前已经有200+社区开发者参与进来，正在火热开发中，欢迎大家踊跃参与进来。</p> 
<p>以下是该项目的源码：</p> 
<p><a href="https://gitee.com/devui/vue-devui">https://gitee.com/devui/vue-devui</a></p> 
<p>参与贡献可以加小助手微信：devui-official，拉你进Vue DevUI核心成员小组～</p> 
<p>以下是Vue DevUI相关的往期文章：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6996217326378942472" target="_blank">Vue DevUI 又新添了11位新成员啦～</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6992233443585163300" target="_blank">Vue DevUI 已经有10个组件成员啦～</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6956988395016945701" target="_blank">让我们一起建设 Vue DevUI 项目吧！</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6995181489960779806" target="_blank">我为 DevUI 开发的脚手架</a></p> 
<h1>致谢</h1> 
<p>感谢所有为DevUI生态建设做出贡献的开发者们，祝大家工作愉快~</p>
                                        </div>
                                      
</div>
            