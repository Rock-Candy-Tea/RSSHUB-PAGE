
---
title: 'vue中的生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a79fbf1abf42748a86cfd56ebe2fef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 22:12:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a79fbf1abf42748a86cfd56ebe2fef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>Vue生命周期 具体执行流程请看文章末尾</p>
</blockquote>
<h2 data-id="heading-0">阶段一  创建期</h2>
<h4 data-id="heading-1"><strong><code>beforeCreate</code>  执行之前初始化事件以及生命周期</strong></h4>
<p>Vue实例在内存中刚被创建，数据对象（data）和方法（methods）未初始化；</p>
<ol>
<li>在这个钩子函数中，不能获取data中的数据</li>
<li>这个函数不能操作DOM</li>
</ol>
<h4 data-id="heading-2"><strong><code>created</code>  进行数据监听</strong></h4>
<p>实例已经在内存中创建好，数据和方法已经初始化完成，但是模板还未编译，页面还是没有内容；（此时访问<code>this.$el</code> 和<code>this.$refs.xxx</code> 都是 <code>undefined</code>）</p>
<ul>
<li>在created发送请求</li>
</ul>
<ol>
<li>可以获取到data中的数据</li>
<li>不能操作DOM</li>
</ol>
<h4 data-id="heading-3"><strong><code>beforeMount</code>  执行之前</strong></h4>
<p>找到对应的template模板，编译成render函数，转换成虚拟dom，此时模板已经编译完成，数据未挂载到页面 <strong>，也就是说在这个阶段你可以看到标签间的双花括号，数据还未渲染到页面中</strong>；</p>
<p><strong>补充：</strong></p>
<h4 data-id="heading-4"><strong><code>render</code> : h=>h(App)</strong></h4>
<p><strong>在beforeMounte之后和mounted之前，还有渲染render函数，它的作用是把模板渲染成虚拟dom</strong></p>
<h4 data-id="heading-5">  <strong><code>mounted</code>  挂载完毕</strong></h4>
<p>模板编译好了，虚拟dom渲染成真正的dom标签，数据渲染到页面，此时Vue实例已经创建完毕，如果没有其他操作的话，Vue实例也没有操作。一般会在mounted中来渲染从后端获取的数据！(页面初始化时，如果有操作dom的事件一般也会放在mounted钩子函数中，当然，你也 可以放在<code>create</code>中，前提需使用<code>this.$nextTick(function()&#123;&#125;)，在回调函数中操作dom</code>。)</p>
<p><strong>--debugger--</strong>
挂载： 把VUE实例生成的虚拟的DOM转成真实的DOM，放在了页面中，这就是挂载； // 编译出的DOM把原有的DOM替换完毕； // 可以获取最终的DOM元素</p>
<h2 data-id="heading-6">阶段二  实例期</h2>
<h4 data-id="heading-7">  <strong><code>beforeUpdate</code>  更新数据之前执行</strong></h4>
<p>当数据更新时，会调用beforeUpdate 和updated钩子函数；上面四个不再运行
更新数据之前执行</p>
<h4 data-id="heading-8">  <strong><code>updated</code>  更新数据之后执行</strong></h4>
<p>数据更新，虚拟的DOM更新，然后更新真实的DOM；最后触发这个函数</p>
<h2 data-id="heading-9">阶段三  销毁期</h2>
<h4 data-id="heading-10">  <strong><code>beforeDestroy</code>  销毁之前</strong></h4>
<ol>
<li>销毁之前</li>
<li>清除定时器</li>
</ol>
<h4 data-id="heading-11">  <strong><code>destroyed</code>  销毁之后</strong></h4>
<ol>
<li>销毁子组件，销毁观察者，事件监听者</li>
<li>元素的事件还在，但是更改数据不会再让视图进行更新了</li>
</ol>


















































<table><thead><tr><th>钩子函数</th><th>触发的行为</th><th>在此阶段可以做的事</th></tr></thead><tbody><tr><td>beforeCreadte</td><td>vue实例的挂载元素$el和数据对象data都为undefined，还未初始化。</td><td>加loading事件</td></tr><tr><td>created</td><td>vue实例的数据对象data有了，$el还没有</td><td>结束loading、请求数据为mounted渲染做准备</td></tr><tr><td>beforeMount</td><td>vue实例的$el和data都初始化了，但还是虚拟的dom节点，具体的data.filter还未替换。</td><td></td></tr><tr><td>mounted</td><td>vue实例挂载完成，data.filter成功渲染</td><td>配合路由钩子使用</td></tr><tr><td>beforeUpdate</td><td>data更新前触发</td><td></td></tr><tr><td>updated</td><td>data更新时触发</td><td>数据更新时，做一些处理（此处也可以用watch进行观测）</td></tr><tr><td>beforeDestroy</td><td>组件销毁时触发</td><td></td></tr><tr><td>destroyed</td><td>组件销毁时触发，vue实例解除了事件监听以及和dom的绑定（无响应了），但DOM节点依旧存在</td><td>组件销毁时进行提示</td></tr></tbody></table>
<p><strong>大图警告！！！！</strong>
<strong>大图警告！！！！</strong>
<strong>大图警告！！！！</strong></p>
<p><strong>大图警告！！！！</strong>
<strong>大图警告！！！！</strong>
<strong>大图警告！！！！</strong></p>
<p><strong>大图警告！！！！</strong>
<strong>大图警告！！！！</strong>
<strong>大图警告！！！！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a79fbf1abf42748a86cfd56ebe2fef~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_42778001%2Farticle%2Fdetails%2F96117236%3Fops_request_misc%3D%26request_id%3D%26biz_id%3D102%26utm_term%3Dvue%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E9%2592%25A9%25E5%25AD%2590%25E5%2587%25BD%25E6%2595%25B0%26utm_medium%3Ddistribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-.nonecase%26spm%3D1018.2226.3001.4187" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_42778001/article/details/96117236?ops_request_misc=&request_id=&biz_id=102&utm_term=vue%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90%E5%87%BD%E6%95%B0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-.nonecase&spm=1018.2226.3001.4187" ref="nofollow noopener noreferrer">文章链接</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23%25E9%2580%2589%25E9%25A1%25B9-%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E9%2592%25A9%25E5%25AD%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90" ref="nofollow noopener noreferrer">官网链接</a></p></div>  
</div>
            