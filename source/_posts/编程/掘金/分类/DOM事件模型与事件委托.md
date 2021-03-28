
---
title: 'DOM事件模型与事件委托'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59bfb16314fb484792d4cf9dce36caad~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 22:13:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59bfb16314fb484792d4cf9dce36caad~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">DOM事件模型与事件委托</h1>
<h2 data-id="heading-1">DOM事件模型</h2>
<p>先看一段代码</p>
<pre><code class="copyable"> <div class="爷爷">
        <div class="爸爸">
            <div class="儿子">文字</div>
        </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给3个div分别添加事件监听fnYe/fnBa/fnEr。有2个问题：</p>
<p><strong>1. 提问1：点击了谁？</strong></p>
<p>点击文字，算不算点击儿子？</p>
<p>点击文字，算不算点击爸爸？</p>
<p>点击文字，算不算点击爷爷？</p>
<p>答案：都算</p>
<p><strong>2. 提问2：调用循序</strong></p>
<p>点击文字，最先调用fnYe/fnBa/fnEr中的那一个函数？</p>
<p>答案：都行。IE5调用顺序为fnEr->fnBa->fnYe, 网景调用顺序为fnYe->fnBa->fnEr。</p>
<p>W3C在2002年发布了标准, 规定浏览器同时支持两种调用顺序.<strong>首先按爷爷->爸爸->儿子顺序看有没有函数监听, 然后按儿子->爸爸->爷爷顺序看有没有函数监听.</strong></p>
<p>专业术语是DOM事件模型的<strong>事件捕获</strong>和<strong>事件冒泡</strong>.一个事件发生后，会在子元素和父元素之间传播（propagation）。</p>
<h3 data-id="heading-2">捕获和冒泡</h3>
<p><strong>由外向内找监听函数, 叫事件捕获.</strong></p>
<p><strong>由内向外找监听函数, 叫事件冒泡.</strong></p>
<ol>
<li>因此DOM事件模型分为3个阶段:</li>
</ol>
<p>（1）捕获阶段：事件从window对象自上而下向目标节点传播的阶段(示例代码中简化为: 爷爷->爸爸->儿子)；</p>
<p>（2）目标阶段：真正的目标节点正在处理事件的阶段；(示例代码中: 文字)</p>
<p>（3）冒泡阶段：事件从目标节点自下而上向window对象传播的阶段(示例代码中简化为: 儿子->爸爸->爷爷)。
<img alt="cSqhdS.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59bfb16314fb484792d4cf9dce36caad~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">addEventListener事件绑定API</h3>
<pre><code class="copyable">IE5*:div1.attachEvent('onclick',fn)//冒泡

网景:div1.addEventListener('click',fn)//捕获

W3C:div1.addEventListener('click',fn,bool)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果bool不传或为falsy</strong></p>
<p>就让fn走冒泡，即当浏览器在冒泡阶段发现baba有fn监听函数，就会调用fn,并提供时间信息。</p>
<p><strong>如果bool为true</strong></p>
<p>就让fn走捕获，即当浏览器在捕获阶段发现baba有fn监听函数，就会调用fn,并且提供事件信息。
<img alt="cSL9zR.png" class="lazyload" src="https://z3.ax1x.com/2021/03/28/cSL9zR.png" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">代码解释</h4>
<p><a href="http://js.jirengu.com/tudiduloci/1/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">代码</a></p>
<h3 data-id="heading-5">e.target 和e.currentTarget区别</h3>
<ol>
<li>区别：</li>
</ol>
<blockquote>
<p>e.target - 用户操作的元素<br>
e.currentTarget-程序员监听的元素<br>
this是e.currentTarget,我个人不推荐使用它</p>
</blockquote>
<ol start="2">
<li>举例：</li>
</ol>
<blockquote>
<p>div>span&#123;文字&#125;,用户点击文字
e.target就是span
e.currentTarget就是div</p>
</blockquote>
<h3 data-id="heading-6">一个监听顺序的特例</h3>
<ol>
<li>背景</li>
</ol>
<blockquote>
<p>只有一个div被监听（不考虑父子同时被监听）</p>
</blockquote>
<blockquote>
<p>fn分别再捕获阶段和冒泡阶段监听click事件</p>
</blockquote>
<blockquote>
<p>用户点击的元素就是开发者监听的</p>
</blockquote>
<ol start="2">
<li>代码</li>
</ol>
<pre><code class="copyable">div.addEventListenter('click',f1)

div.addEventListenter('click',f2,true)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请问，f1先执行还是f2先执行？如果把两个调换位置？
3. 答案
谁先监听谁先执行。</p>
<h3 data-id="heading-7">取消冒泡和阻止默认事件</h3>
<h4 data-id="heading-8">取消冒泡</h4>
<p><strong>捕获不可取消，但冒泡可以</strong></p>
<ol>
<li>event.stopPropagation()可中断冒泡，浏览器不再向上走。</li>
</ol>
<p>【W3C标准event.stopPropagation()；但不支持IE9以下版本】
【IE独有(谷歌也实现了)event.cancelBubble = true;】</p>
<ol start="2">
<li>一般用于封装某些独立的组件</li>
<li>Bubbles ——该事件是否冒泡，所有冒泡都可取消</li>
<li>Cancelable ——是否支持开发者阻止默认事件</li>
</ol>
<h4 data-id="heading-9">阻止默认事件</h4>
<ol>
<li>默认事件——表单提交，a标签跳转，右键菜单等</li>
<li>方法：</li>
</ol>
<pre><code class="copyable">return false；以对象属性的方式注册的时间才生效
event.preventDefault()W3C标注，IE9以下不兼容
event.returnValue = false；兼容IE
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">事件委托</h2>
<h3 data-id="heading-11">自定义事件</h3>
<ol>
<li>浏览器的自定义事件。<a href="https://developer.mozilla.org/zh-CN/docs/Web/Events" target="_blank" rel="nofollow noopener noreferrer">MDN列表</a>。</li>
<li>自定义事件：<a href="http://js.jirengu.com/wihoqenifi/1/edit?html,js,console,output" target="_blank" rel="nofollow noopener noreferrer">例子</a></li>
</ol>
<h3 data-id="heading-12">事件委托</h3>
<p><strong>“事件代理”即是把原本需要绑定在子元素的响应事件（click、keydown......）委托给父元素，让父元素担当事件监听的职务。事件代理的原理是DOM元素的事件冒泡</strong></p>
<p><a href="https://blog.csdn.net/qq_38128179/article/details/86293394" target="_blank" rel="nofollow noopener noreferrer">参考一个文章</a></p>
<h3 data-id="heading-13">应用场景</h3>
<ol>
<li>场景1：</li>
</ol>
<p>要给100个按钮添加点击事件，咋办？</p>
<p>答：监听这个100个按钮的祖先，等冒泡的时候判断target是不是这100个按钮中的一个</p>
<p><a href="http://js.jirengu.com/kewizokute/1/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">代码</a></p>
<ol start="2">
<li>场景2：</li>
</ol>
<p>你要监听目前不存在的元素的点击事件？</p>
<p>答：监听祖先，等点击的时候看看是不是监听的元素即可。</p>
<p><a href="http://js.jirengu.com/kuyugibeno/1/edit?html,js,console,output" target="_blank" rel="nofollow noopener noreferrer">代码</a></p>
<h4 data-id="heading-14">优点</h4>
<ol>
<li>省监听数（内存）：可以大量节省内存占用，减少事件注册，比如在ul上代理所有li的click事件就非常棒。</li>
<li>可以动态监听元素： 可以实现当新增子对象时无需再次对其绑定（动态绑定事件）</li>
</ol>
<h4 data-id="heading-15">封装一个事件委托</h4>
<ol>
<li>要求：实现一个on('click','#testDiv','li',fn)函数，要求可以实现事件委托。当用户点击#testDiv里面的li元素时，调用fn函数。</li>
<li><a href="http://js.jirengu.com/tanuvovuzo/1/edit?html,js,console,output" target="_blank" rel="nofollow noopener noreferrer">代码</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            