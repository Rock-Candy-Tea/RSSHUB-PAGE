
---
title: '上手后才知道 ，Vue3 的 script setup 语法糖是真的爽'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8187'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 03:17:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=8187'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">点击查看：后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>还记得刚体验 script setup 语法糖的时候，编辑器提示我这是一个实验性的提案，要使用的话，需要固定 Vue 版本。</p>
<p>而在 6 月底，该提案被正式定稿，在 v3.1.3 的版本上，你可以继续使用但仍会有实验性提案的提示，在 v3.2 中，才会去除提示并移除一些废弃的 API。</p>
<h3 data-id="heading-0">script setup 是个啥？</h3>
<p>它是 Vue3 的一个新语法糖，在 <code>setup</code> 函数中。所有 ES 模块导出都被认为是暴露给上下文的值，并包含在 setup() 返回对象中。相对于之前的写法，使用后，语法也变得更简单。</p>
<p>使用方式极其简单，仅需要在 <code>script</code> 标签加上 <code>setup</code> 关键字即可。示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><script setup></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">组件自动注册</h3>
<p>在 script setup 中，引入的组件可以直接使用，无需再通过<code>components</code>进行注册，并且无法指定当前组件的名字，它会自动以文件名为主，也就是不用再写<code>name</code>属性了。示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> /></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Child <span class="hljs-keyword">from</span> <span class="hljs-string">'./Child.vue'</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要定义类似 name 的属性，可以再加个平级的 script 标签，在里面实现即可。</p>
<h3 data-id="heading-2">组件核心 API 的使用</h3>
<h4 data-id="heading-3">使用 props</h4>
<p>通过<code>defineProps</code>指定当前 props 类型，获得上下文的props对象。示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><script setup>
  <span class="hljs-keyword">import</span> &#123; defineProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

  <span class="hljs-keyword">const</span> props = defineProps(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>,
  &#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">使用 emits</h4>
<p>使用<code>defineEmit</code>定义当前组件含有的事件，并通过返回的上下文去执行 emit。示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><script setup>
  <span class="hljs-keyword">import</span> &#123; defineEmits &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

  <span class="hljs-keyword">const</span> emit = defineEmits([<span class="hljs-string">'change'</span>, <span class="hljs-string">'delete'</span>])
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">获取 slots 和 attrs</h4>
<p>可以通过<code>useContext</code>从上下文中获取 slots 和 attrs。不过提案在正式通过后，废除了这个语法，被拆分成了<code>useAttrs</code>和<code>useSlots</code>。示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 旧</span>
<script setup>
  <span class="hljs-keyword">import</span> &#123; useContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

  <span class="hljs-keyword">const</span> &#123; slots, attrs &#125; = useContext()
</script>

<span class="hljs-comment">// 新</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; useAttrs, useSlots &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

  <span class="hljs-keyword">const</span> attrs = useAttrs()
  <span class="hljs-keyword">const</span> slots = useSlots()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">defineExpose API</h3>
<p>传统的写法，我们可以在父组件中，通过 ref 实例的方式去访问子组件的内容，但在 script setup 中，该方法就不能用了，setup 相当于是一个闭包，除了内部的 <code>template</code>模板，谁都不能访问内部的数据和方法。</p>
<p>如果需要对外暴露 setup 中的数据和方法，需要使用 defineExpose API。示例：</p>
<pre><code class="copyable"><script setup>
import &#123; defineExpose &#125; from 'vue'
const a = 1
const b = 2
defineExpose(&#123;
    a
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">属性和方法无需返回，直接使用！</h4>
<p>这可能是带来的较大便利之一，在以往的写法中，定义数据和方法，都需要在结尾 return 出去，才能在模板中使用。在 script setup 中，定义的属性和方法无需返回，可以直接使用！示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span>></span>My name is &#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;

<span class="hljs-keyword">const</span> name = ref(<span class="hljs-string">'Sam'</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">写在最后</h3>
<p>写作不易，希望可以获得你的一个「赞」。如果文章对你有用，可以选择「收藏」。
如有文章有错误或建议，欢迎评论指正，谢谢你。❤️</p>
<h4 data-id="heading-9">欢迎阅读其它文章</h4>
<ul>
<li><a href="https://juejin.cn/post/6975770170413776926" target="_blank" title="https://juejin.cn/post/6975770170413776926">实战：用 Vue3 实现一个 Message 消息组件</a></li>
<li><a href="https://juejin.cn/post/6981232153233195039" target="_blank" title="https://juejin.cn/post/6981232153233195039">实战：用 Vue3 实现 Image 组件，顺便支持懒加载</a></li>
<li><a href="https://juejin.cn/post/6968352814858764296" target="_blank" title="https://juejin.cn/post/6968352814858764296">One Piece，Vue.js 3.0 带来了哪些更新</a></li>
<li><a href="https://juejin.cn/post/6983625803271503886/" target="_blank" title="https://juejin.cn/post/6983625803271503886/">一篇文章消化 ES7、ES8、ES9 主要新特性</a></li>
<li><a href="https://juejin.cn/post/6979053938087723021" target="_blank" title="https://juejin.cn/post/6979053938087723021">技术团队普遍存在的问题和解决方案</a></li>
<li><a href="https://juejin.cn/post/6844903618810757128" target="_blank" title="https://juejin.cn/post/6844903618810757128">ES6中常用的10个新特性讲解</a></li>
</ul></div>  
</div>
            