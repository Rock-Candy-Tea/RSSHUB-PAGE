
---
title: '基于Vue的架构设计'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5e09865a9b42e3b25e8405bf614c9e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:18:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5e09865a9b42e3b25e8405bf614c9e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>架构包含非常广泛的概念与内容，架构的核心目的是为了提高效率、降低成本、保障质量， 同时需要结合实际业务情况综合考虑，为未来提供可持续发展空间。<br>
目前在公司我负责做一个运维服务云平台中后台管理系统的前端架构开发工作，公司内部目前主要使用的技术栈是Vue，但是并没有非常适合我们项目需求的的工程模板，因此在原有框架的基础上根据项目实际情况进行优化升级，符合实际项目需求。</p>
<h1 data-id="heading-1">技术选型</h1>
<p>在技术选型阶段，需要考虑公司内部采用的技术栈以及团队成员的技术栈，目前公司内部主流的技术栈方向是Vue,所以我们选择Vue作为前端主要技术框架。</p>
<ul>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>脚手架：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;脚手架：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">脚</span><span class="mord cjk_fallback" style="color:red;">手</span><span class="mord cjk_fallback" style="color:red;">架</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>围绕Vue技术栈，我们采用Vue CLI脚手架工具来快速构建基础工程。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mi>U</mi><mi>I</mi><mtext>组件库：</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;UI组件库：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord mathnormal" style="margin-right:0.10903em;color:red;">U</span><span class="mord mathnormal" style="margin-right:0.07847em;color:red;">I</span><span class="mord cjk_fallback" style="color:red;">组</span><span class="mord cjk_fallback" style="color:red;">件</span><span class="mord cjk_fallback" style="color:red;">库</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>为了提高开发效率避免重复造轮子，我们需要选择一套现有的UI组件库，我们选择了目前主流的ElementUI。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>路由管理：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;路由管理：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">路</span><span class="mord cjk_fallback" style="color:red;">由</span><span class="mord cjk_fallback" style="color:red;">管</span><span class="mord cjk_fallback" style="color:red;">理</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>路由控制采用Vue Router。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>状态管理：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;状态管理：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">状</span><span class="mord cjk_fallback" style="color:red;">态</span><span class="mord cjk_fallback" style="color:red;">管</span><span class="mord cjk_fallback" style="color:red;">理</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>统一集中管理项目中组件状态采用Vuex。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>异步请求：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;异步请求：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">异</span><span class="mord cjk_fallback" style="color:red;">步</span><span class="mord cjk_fallback" style="color:red;">请</span><span class="mord cjk_fallback" style="color:red;">求</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>异步请求采用axios。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>样式管理：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;样式管理：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">样</span><span class="mord cjk_fallback" style="color:red;">式</span><span class="mord cjk_fallback" style="color:red;">管</span><span class="mord cjk_fallback" style="color:red;">理</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>样式管理采用scss。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>静态资源：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;静态资源：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">静</span><span class="mord cjk_fallback" style="color:red;">态</span><span class="mord cjk_fallback" style="color:red;">资</span><span class="mord cjk_fallback" style="color:red;">源</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>静态资源图标等采用svg图标。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>工具库：</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;工具库：&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">工</span><span class="mord cjk_fallback" style="color:red;">具</span><span class="mord cjk_fallback" style="color:red;">库</span><span class="mord cjk_fallback" style="color:red;">：</span></span></span></span></span></span>为了提高开发效率，降低JS中数组、对象、字符串、日期等等使用难度，我们采用了Lodash、dayjs。</p>
</li>
</ul>
<h1 data-id="heading-2">开发规范</h1>
<p>事先制定一个统一的代码风格、命名规则、目录结构、静态资源使用规范，可以显著提高开发效率、开发质量；在这里主要从以下几方面进行规范管理。</p>
<ul>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>开发工具</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;开发工具&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">开</span><span class="mord cjk_fallback" style="color:red;">发</span><span class="mord cjk_fallback" style="color:red;">工</span><span class="mord cjk_fallback" style="color:red;">具</span></span></span></span></span></span><br>
每个人习惯使用的IDE不同，可能导致出现不同的开发风格，尽量统一开发工具，我们这里采用VS Code进行前端编码开发工作(同时也可以通过配置editorconfig的方式来支持不同IDE统一代码风格)。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mi>E</mi><mi>S</mi><mi>L</mi><mi>i</mi><mi>n</mi><mi>t</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;ESLint&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord mathnormal" style="margin-right:0.05764em;color:red;">E</span><span class="mord mathnormal" style="margin-right:0.05764em;color:red;">S</span><span class="mord mathnormal" style="color:red;">L</span><span class="mord mathnormal" style="color:red;">i</span><span class="mord mathnormal" style="color:red;">n</span><span class="mord mathnormal" style="color:red;">t</span></span></span></span></span></span><br>
编码过程中，代码规范很重要，可以避免很多编码错误，提高代码可读性，我们采用Airbnb JavaScript 这套代码规范。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mi>p</mi><mi>r</mi><mi>e</mi><mi>t</mi><mi>t</mi><mi>i</mi><mi>e</mi><mi>r</mi></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;prettier&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.85396em;vertical-align:-0.19444em;"></span><span class="mord" style="color:red;"><span class="mord mathnormal" style="color:red;">p</span><span class="mord mathnormal" style="margin-right:0.02778em;color:red;">r</span><span class="mord mathnormal" style="color:red;">e</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="color:red;">i</span><span class="mord mathnormal" style="color:red;">e</span><span class="mord mathnormal" style="margin-right:0.02778em;color:red;">r</span></span></span></span></span></span><br>
我们采用Vetur插件来实现代码质量提示&错误、格式化/风格、智能提示格式化。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>静态资源</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;静态资源&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">静</span><span class="mord cjk_fallback" style="color:red;">态</span><span class="mord cjk_fallback" style="color:red;">资</span><span class="mord cjk_fallback" style="color:red;">源</span></span></span></span></span></span><br>
对静态资源的管理，在开发过程中，经常会用到大量图标，这里我们选择使用 SVG 图标。</p>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>代码规范</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;代码规范&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">代</span><span class="mord cjk_fallback" style="color:red;">码</span><span class="mord cjk_fallback" style="color:red;">规</span><span class="mord cjk_fallback" style="color:red;">范</span></span></span></span></span></span><br></p>
<ol>
<li>
<p>统一使用2占位符缩进。</p>
</li>
<li>
<p>统一使用UTF-8字符编码。</p>
</li>
<li>
<p>js代码最外层统一使用单引号。</p>
</li>
<li>
<p>js代码末尾不需要加分号。</p>
</li>
<li>
<p>变量命名采用驼峰式命名，常量全大写。</p>
</li>
<li>
<p>data的使用，在组建中使用data属性的时候，data选项必须是一个函数。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>prop定义时，至少需要指定其类型。</p>
<pre><code class="hljs language-js copyable" lang="js">  props: &#123;
    <span class="hljs-attr">attr</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> &#123;&#125;
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>v-if和v-for不能同时使用，可以采用computed的方式对v-for的数据进行过滤。</p>
<pre><code class="hljs language-js copyable" lang="js">错误的示例：
<div v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"item in message"</span> v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"item!=='a'"</span>></div>

正确的示例：
<div v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"item in getMessage"</span>></div>
computed: &#123;
  getMessage () &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.message.filter(<span class="hljs-function"><span class="hljs-params">res</span>=></span>res!==<span class="hljs-string">'a'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>computed中禁止对变量进行修改操作。</p>
</li>
<li>
<p>公共方法抽取封装到utils文件目录中。</p>
</li>
<li>
<p>使用prop传参时，不要改变prop参数的值，可以采用emit方式修改参数值。</p>
</li>
<li>
<p>修改vuex中数据必须通过mutations。</p>
</li>
<li>
<p>可以通过getters获取需要的数据格式。</p>
</li>
<li>
<p>和服务端交互的数据接口尽量在actions中调用，获取的数据通过mutations改变state。</p>
</li>
<li>
<p>组件特有样式必须设置独立作用域。</p>
</li>
</ol>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>命名规则</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;命名规则&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">命</span><span class="mord cjk_fallback" style="color:red;">名</span><span class="mord cjk_fallback" style="color:red;">规</span><span class="mord cjk_fallback" style="color:red;">则</span></span></span></span></span></span></p>
<ol>
<li>
<p>文件夹命名<br>
采用小驼峰命名法;<br>
例如：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>productList, productDetail</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;productList, productDetail&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">p</span><span class="mord textrm" style="color:red;">r</span><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">d</span><span class="mord textrm" style="color:red;">u</span><span class="mord textrm" style="color:red;">c</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">L</span><span class="mord textrm" style="color:red;">i</span><span class="mord textrm" style="color:red;">s</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">,</span><span class="mord textrm" style="color:red;"> </span><span class="mord textrm" style="color:red;">p</span><span class="mord textrm" style="color:red;">r</span><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">d</span><span class="mord textrm" style="color:red;">u</span><span class="mord textrm" style="color:red;">c</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">D</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">a</span><span class="mord textrm" style="color:red;">i</span><span class="mord textrm" style="color:red;">l</span></span></span></span></span></span></span><br>
复数结构时，采用复数命名法；<br>
例如：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>pages, views, utils</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;pages, views, utils&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">p</span><span class="mord textrm" style="color:red;">a</span><span class="mord textrm" style="color:red;">g</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">s</span><span class="mord textrm" style="color:red;">,</span><span class="mord textrm" style="color:red;"> </span><span class="mord textrm" style="color:red;">v</span><span class="mord textrm" style="color:red;">i</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">w</span><span class="mord textrm" style="color:red;">s</span><span class="mord textrm" style="color:red;">,</span><span class="mord textrm" style="color:red;"> </span><span class="mord textrm" style="color:red;">u</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">i</span><span class="mord textrm" style="color:red;">l</span><span class="mord textrm" style="color:red;">s</span></span></span></span></span></span></span><br></p>
</li>
<li>
<p>Vue组件命名<br>
采用官方推荐的大驼峰命名法；<br>
例如：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>MyComponent.vue</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;MyComponent.vue&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">M</span><span class="mord textrm" style="color:red;">y</span><span class="mord textrm" style="color:red;">C</span><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">m</span><span class="mord textrm" style="color:red;">p</span><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">n</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">n</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">.</span><span class="mord textrm" style="color:red;">v</span><span class="mord textrm" style="color:red;">u</span><span class="mord textrm" style="color:red;">e</span></span></span></span></span></span></span></p>
</li>
<li>
<p>Prop参数命名<br>
采用小驼峰命名法；<br>
例如：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>orderId</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;orderId&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">r</span><span class="mord textrm" style="color:red;">d</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">r</span><span class="mord textrm" style="color:red;">I</span><span class="mord textrm" style="color:red;">d</span></span></span></span></span></span></span></p>
</li>
<li>
<p>method自定义函数命名<br>
采用小驼峰命名法；<br>
前缀应该为动词；<br>
例如：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>isNaN, getData</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;isNaN, getData&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">i</span><span class="mord textrm" style="color:red;">s</span><span class="mord textrm" style="color:red;">N</span><span class="mord textrm" style="color:red;">a</span><span class="mord textrm" style="color:red;">N</span><span class="mord textrm" style="color:red;">,</span><span class="mord textrm" style="color:red;"> </span><span class="mord textrm" style="color:red;">g</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">D</span><span class="mord textrm" style="color:red;">a</span><span class="mord textrm" style="color:red;">t</span><span class="mord textrm" style="color:red;">a</span></span></span></span></span></span></span><br></p>
</li>
<li>
<p>data属性命名<br>
采用小驼峰命名法；<br>
例如：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>orderId</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;orderId&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">r</span><span class="mord textrm" style="color:red;">d</span><span class="mord textrm" style="color:red;">e</span><span class="mord textrm" style="color:red;">r</span><span class="mord textrm" style="color:red;">I</span><span class="mord textrm" style="color:red;">d</span></span></span></span></span></span></span></p>
</li>
</ol>
</li>
</ul>
<h1 data-id="heading-3">流程规范</h1>
<p>需求迭代、开发、测试、上线的流程规范;研发如果没有完善的流程规范，项目快做完了可能自己都不一定清楚自己开发了哪些功能，管理上也会导致混乱。大致流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5e09865a9b42e3b25e8405bf614c9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">GIT规范</h1>
<p>GIT版本、分支、代码提交日志规范；采用内部搭建GitLab管理公司项目代码。<br></p>
<ul>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>分支管理</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;分支管理&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">分</span><span class="mord cjk_fallback" style="color:red;">支</span><span class="mord cjk_fallback" style="color:red;">管</span><span class="mord cjk_fallback" style="color:red;">理</span></span></span></span></span></span><br></p>
<ol>
<li>master主分支 <br>
用于生产部署，一般由 uat 分支合并，任何情况下不允许直接在 master 分支上修改代码。<br></li>
<li>uat分支 <br>
预上线分支，提供生产环境下用户测试使用;始终保持与 master 分支一致，一般由 sit 分支合并，不建议直接在此分支上直接修改代码，。<br></li>
<li>sit分支<br>
测试分支，用于测试环境测试使用，根据项目需求大小来确定是否直接在此分支开发或者在开发者本地分支上进行开发。</li>
<li>dev分支<br>
开发分支，用于开发新需求，需求上线发布成功后，开发人员删除此分支。</li>
</ol>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>版本管理</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;版本管理&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">版</span><span class="mord cjk_fallback" style="color:red;">本</span><span class="mord cjk_fallback" style="color:red;">管</span><span class="mord cjk_fallback" style="color:red;">理</span></span></span></span></span></span><br></p>
<ol>
<li>版本号使用x.x.x进行定义.</li>
<li>第一个X代表大版本，一个大迭代代表一个版本。 <br></li>
<li>第二个X代表小版本，一个大迭代可以分成几个小版本。 <br></li>
<li>第三个X代表线上BUG修正。<br></li>
</ol>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>日志规范</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;日志规范&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">日</span><span class="mord cjk_fallback" style="color:red;">志</span><span class="mord cjk_fallback" style="color:red;">规</span><span class="mord cjk_fallback" style="color:red;">范</span></span></span></span></span></span><br>
为了方便项目管理，git commit 信息最好按照一定的格式规范，使用良好的Commit Message有利于代码审查，能更快速查找变更记录。规范格式如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>type为必填项，用于指定commit的类型.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">常用type：
    feat：新曾功能或功能变更
    fix：修复bug
其他type:    
    docs：文档提交
    build：修改项目的的构建工具或外部依赖（webpack、glup等）
    style：主要是样式方面的优化、如删除空格、改变缩进、单双引号切换等，并不会影响代码逻辑的修改
    refactor：代码重构
    revert：回滚某个更早的提交
    ci：修改项目的持续集成流程（Kenkins、Travis等）的提交
    chore：构建过程或辅助工具的变化
    pref：性能、体验相关的提交
    test：测试相关的开发
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>subject.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">commit的简短描述，如果有团队管理工具(issue ,JIRA)等，以内部命名的需求代号作为描述信息的一部分。
举例：
<span class="hljs-attr">feat</span>:##需求代号 开发XXX需求
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>body.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">body填写详细描述，针对比较重要或复杂的情况进行详细描述。
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>footer.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">备注, 通常是 BREAKING CHANGE 或修复的 bug 的链接。
例如：
Closes XX-<span class="hljs-number">0001</span>
fix #JIRA_ID
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>未完待续</p></div>  
</div>
            