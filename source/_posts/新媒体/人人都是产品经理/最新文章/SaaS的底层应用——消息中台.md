
---
title: 'SaaS的底层应用——消息中台'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/b5v30IsRva4fqiH9nHkI.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 11 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/b5v30IsRva4fqiH9nHkI.jpg'
---

<div>   
<blockquote><p>编辑导语：作为SaaS的底层应用——消息中台，它能最大程度减少开发资源的浪费与重复造轮子的问题，同时也对于各种业态都有极强的适应性。作者以“短信”、“邮件”、“微信”三个平台为例，向我们解释了消息中台的选择、价值和原则等方面内容。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5350298" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/b5v30IsRva4fqiH9nHkI.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>随着业务越来越多，消息模版以及第三方推送都是存在于代码的配置文件中，这样的操作比较繁琐也不容易管理，于是就决定研发系统来将各类推送消息聚合至前台，其事务与推送渠道规则由产品配置决定。</p>
<p>其次，作为SaaS产品的发展必须支持其它业务平台的接入，而接入之后的账号体系和消息推送打通尤为重要。因此作为建筑设计领域平台，会有提供第三方开放平台的诉求。</p>
<h2 id="toc-1"><strong>一、需求分析</strong></h2>
<ul>
<li>为满足不同业务平台提供消息系统的支撑，帮助不同业务系统完成基础消息的闭环流程。</li>
<li>支持产品配置业务类消息模版，及相应媒介。支持运营配置营销类消息模板，及相应媒介。</li>
<li>对接汇聚各类消息触达媒介，支持多类事件调用。</li>
</ul>
<h3><strong>1. 好处</strong></h3>
<ul>
<li>所有账号密码都是存在代码于配置文件中，一旦出现密码泄露等情况，那么就需要重新上线，风险性较高。</li>
<li>支持单一消息通道出现异常后，消息中台就会使用通道切换策略，确保不会影响用户正常的使用。</li>
<li>消息中台使用异步发送的机制，提高吞吐量、并发量。即确保消息将第一时间触达至用户。</li>
<li>对消息数据进行沉淀，可用于后期进行数据分析。</li>
</ul>
<h3><strong>2. 价值</strong></h3>
<ul>
<li><strong>开发成本：</strong>最大程度地完成消息分发系统与业务系统的解耦，最大程度减少开发资源的浪费与重复造轮子的问题。</li>
<li><strong>拓展性：</strong>与放在业务系统单独开发不同，消息中台可接入各类消息媒介接口，建立消息模板体系，具备极强横向扩展属性；同时也为后续开放平台提供支撑、低代码工作流业务赋能。</li>
<li><strong>适应性：</strong>消息中台对于各种业态有极强的适应性，这也是得力于其仅仅承担了业务当中消息分发的能力。</li>
</ul>
<h2 id="toc-2"><strong>二、消息推送媒介的选择</strong></h2>
<h3>1. 短信</h3>
<p><strong>短信服务：</strong>21世纪的今天，几乎人人都有手机，作为目前消息推送的主流之一，短信的触达率是最高的。</p>
<p>主流短信服务商对短信的收费标准在¥0.05 元/条左右，频繁的推送会是不小的成本，也会造成短信轰炸。</p>
<p>所以这类渠道一般用于验证码、系统通知、营销短信业务的使用。</p>
<h3>2. 邮件</h3>
<p><strong>邮件服务：</strong>基本上人人都会有邮件，与短信不同的是，邮件是不需要向邮件服务商付费的，邮件触达率较低，对用户造成的困扰较低，所以，对于营销类的使用更为友好。</p>
<p>另外，邮件是可以作为除了短信通道之外的验证入口。</p>
<h3>3. 微信</h3>
<p><strong>微信推送服务：</strong>截止2020年底，目前国内微信拥有11亿多用户量，对于国内用户来说微信推送是目前除了短信推送触达率最高的渠道之一。</p>
<p>而微信推送包括的小程序和公众号推送，几乎是不需要成本。虽然推送会有内容方面的限制，但是我们推送的大部分内容是与用户互动的业务消息，是用户愿意主动接受的消息。</p>
<p>所以这类渠道，我们一般用于业务消息以及与用户产生互动的推送。</p>
<h2 id="toc-3"><strong>三、消息分发流程</strong></h2>
<ul>
<li><strong>发送方：</strong>消息内容（消息类型、消息模板）、消息对象（系统范围内的人员）</li>
<li><strong>媒介方：</strong>消息策略（触达媒介选择：短信、邮件、站内信、微信等 ，消息任务时限设置，消息补发策略）、消息管理（增删查改）</li>
<li><strong>触达方：</strong>消息回执（已读未读、数据反馈回流）</li>
</ul>
<h2 id="toc-4"><strong>四、接口文档（平台）</strong></h2>
<p>与RD定义所需开放接口，以及回调方式，这个可作为后期考虑。</p>
<h2 id="toc-5"><strong>五、媒介</strong></h2>
<h3><strong>1. 微信</strong></h3>
<p>主要使用微信服务号推送媒介，绑定微信服务号获取API key，对接微信提供的相应接口，以实现在消息中台统一配置管理的目的。</p>
<p><strong>注：</strong>公有模版库内没有的，需提交审核，一般使用公有模版库即可满足需求。</p>
<p>从公共模板库中选用模板，到私有模板库中，之后可以直接在创建业务时，调用模板，根据业务进行自定义配置。</p>
<p>消息模板内容形式，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/bQdxCNhV9Ygl5z0UTMB0.png" alt width="724" height="283" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/ynfDKNbC8YvN0DrcyVMW.jpg" alt width="353" height="372" referrerpolicy="no-referrer"></p>
<h3>2. 短信</h3>
<p>主要选择第三方短信服务商，绑定短信服务商获取APIKey后，对接服务商提供的相应接口，以实现在消息中台统一配置管理的目的。</p>
<p><strong>注：</strong>所使用的消息模板必须通过供应商审核。</p>
<p>短信内容由：签名+消息模板内容（结合业务字段）组成。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/Roce4kCovxcovSEFiMQJ.jpg" alt width="687" height="276" referrerpolicy="no-referrer"></p>
<h3><strong>3. 邮件</strong></h3>
<p>应支持接入主流邮件服务商（例如：qq、163、腾讯企业邮箱、阿里企业邮箱），完成之后可供业务调用邮件推送媒介时选取，进行自定义配置。以实现在消息中台统一配置管理的目的。</p>
<p>创建邮件服务程序时输入以下内容即可完成接入：</p>
<ul>
<li>host：邮箱传输服务器</li>
<li>username：用户名 （登录邮件的用户名）</li>
<li>password：密码（登录邮件的密码）</li>
</ul>
<p>以上配置为发送方邮箱认证，还需配置发送方名称，具体例子如下图使示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/iKSswZ1TEAhCdBPAa3HQ.png" alt width="707" height="303" referrerpolicy="no-referrer"></p>
<h2 id="toc-6"><strong>六、设计原则</strong></h2>
<ul>
<li>不让用户错过重要消息。</li>
<li>在不干扰用户的情况下，达到营销目的。</li>
</ul>
<p>参考资料：</p>
<p>http://www.woshipm.com/pd/5310298.html</p>
<p> </p>
<p>本文由@高姿态 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5348642" data-author="219885" data-avatar="https://static.woshipm.com/woshipm_def_head.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            