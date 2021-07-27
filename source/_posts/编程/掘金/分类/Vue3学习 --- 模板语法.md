
---
title: 'Vue3学习 --- 模板语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5293'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 04:46:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=5293'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">模板语法</h3>
<p>在React使用的jsx，所以对应的代码都是编写的类似于将HTML嵌入到js中的一种语法，之后需要通过Babel将jsx编译成 React.createElement 函数调用。</p>
<p>Vue也支持jsx的开发模式，但是大多数情况下，使用基于HTML的模板语法。</p>
<p>在模板中，允许开发者以声明式的方式将DOM和底层组件实例的数据绑定在一起（mustache语法在模板中绑定对应data）</p>
<p>在底层的实现中，Vue会将模板编译成虚拟DOM渲染函数进行调用</p>
<h4 data-id="heading-1">Mustache语法</h4>
<p>如果我们希望把数据显示到模板(template)中，使用最多的语法是 <strong>“Mustache”语法 (双大括号)</strong> 的文本插值</p>
<p>data返回的对象是有添加到Vue的响应式系统中，因此当data中的数据发生改变时，对应的内容也会自动发生更新。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- 1. 基本使用 -->
<h2>&#123;&#123; msg &#125;&#125;</h2>

<!-- 2. 可以同时使用多个mustache -->
<h2>&#123;&#123; msg &#125;&#125; --- &#123;&#123; msg &#125;&#125;</h2>

<!-- 3. mustache中可以使用任何合法的js表达式 -->
<h2>&#123;&#123; msg.toUpperCase() &#125;&#125;</h2>
<h2>&#123;&#123; isLogin ? 'Login Out': 'Login In' &#125;&#125;</h2>

<!-- 4. 可以在mustache中调用函数和使用计算属性 -->
<h2>&#123;&#123; reverseMsg &#125;&#125;</h2>
<h2>&#123;&#123; getReverseMsg() &#125;&#125;</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">常见指令</h4>
<h5 data-id="heading-3">v-once</h5>
<p>v-once用于指定元素或者组件只渲染一次</p>
<p>当数据发生变化时，<code>元素或者组件以及其所有的子元素</code>将视为<code>静态内容</code>并且跳过</p>
<p>该指令可以用于<code>性能优化</code></p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- count值不会发生改变 -->
<h2 v-once>&#123;&#123; count &#125;&#125;</h2>

<!-- 元素及其子元素都不会再重新渲染 -->
<div v-once>
  <h2>&#123;&#123; count &#125;&#125;</h2>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">v-text</h5>
<pre><code class="hljs language-vue copyable" lang="vue"><h2>&#123;&#123; msg &#125;&#125;</h2>

<!-- 等价于 -->
<h2 v-text="msg"></h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">v-html</h5>
<p>vue在解析模板的时候，会将data中的数据当做字符串进行解析</p>
<p>如果data中的数据是一段html标签的时候，vue依旧会将其作为字符串去进行渲染</p>
<p>如果需要vue将其作为html标签去渲染的时候，可以使用<code>v-html</code></p>
<p>但是因为这段数据可能来自于第三方，所以为了避免<code>XSS攻击</code>，请确保这些数据的可靠性</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!--<h2>Hello World</h2> -->
<h2>&#123;&#123; msg &#125;&#125;</h2>

<!-- Hello World -->
<h2 v-html="msg"></h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">v-pre</h5>
<p>v-pre用于跳过元素和它的子元素的编译过程，显示原始的Mustache标签</p>
<p>v-pre可以跳过不需要编译的节点，加快编译的速度</p>
<pre><code class="hljs language-vue copyable" lang="vue"><h2 v-pre>&#123;&#123; msg &#125;&#125;</h2>
<h2>&#123;&#123; msg &#125;&#125;</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">v-bind</h5>
<p>V-bind ---> 可以动态绑定属性 ---> 动态地绑定一个或多个 attribute，或一个组件 prop 到表达式</p>
<pre><code class="hljs language-vue copyable" lang="vue"><a v-bind:href="link">google</a>

<!-- 简写 ===> 语法糖 -->
<a :href="link">google</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用v-bind绑定class</code></p>
<ol>
<li>
<p>普通绑定</p>
<pre><code class="hljs language-vue copyable" lang="vue"><span :class="active">Hello World</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>对象语法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 对象语法: &#123;样式: boolean值&#125; boolean值为true的时候，会显示样式， 为false的时候，不显示样式 --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;active: isActive&#125;"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

<span class="hljs-comment"><!-- 对象中的key可以是变量 --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;[active]: isActive&#125;"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

<span class="hljs-comment"><!-- 也可以有多个键值对 --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;active: isActive, foo: isFoo&#125;"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

<span class="hljs-comment"><!-- 默认的class和动态的class结合 --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"foo"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;active: isActive&#125;"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

<span class="hljs-comment"><!-- 抽离为一个单独的对象 --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"classObj"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

<span class="hljs-comment"><!-- 抽离为方法或计算属性 --></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"getClassObj()"</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>数组语法</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- 数组中可以是字符串，也可以是变量 -->
<h2 :class="['foo', active]">Hello World</h2>

<!-- 可以是三目运算符 -->
<h2 :class="['foo', isActive ? 'active' : '']">Hello World</h2>

<!-- 数组中某一项的返回值是boolean，无论是true还是false，这一项就不会在样式中显示 -->
<h2 :class="['foo', isActive && 'active']">Hello World</h2>

<!-- 数组中可以嵌套对象语法 -->
<h2 :class="['foo', &#123; 'active': isActive &#125;]">Hello World</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><code>使用v-bind绑定style</code></p>
<p>可以利用v-bind:style来绑定一些CSS内联样式</p>
<p>CSS property 名可以用<code>驼峰式 (camelCase)</code> 或<code>短横线分隔 (kebab-case，记得用引号括起来)</code> 来命名</p>
<ol>
<li>
<p>对象语法</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- 属性值要使用字符串包裹，不然会被作为变量去进行解析 -->
<h2 :style="&#123;color: 'red', backgroundColor: 'gray'&#125;">Hello World</h2>

<!-- 属性名可以使用驼峰或短划法，如果是短划线需要使用引号将属性名进行包裹 -->
<h2 :style="&#123;color: 'red', 'background-color': 'gray'&#125;">Hello World</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>数组语法</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- 对象数组中的每一项都是一个style对象，可以直接写，也可以抽离成一个对象来引用 -->
<h2 :style="[&#123;color: 'red'&#125;, &#123;backgroundColor: 'gray'&#125;]">Hello World</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><code>动态绑定属性</code></p>
<p>如果属性名称不是固定的，我们可以使用 :[属性名]=“值” 的格式来定义</p>
<p>这种绑定的方式，我们称之为动态绑定属性</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!--
    1. 属性名 要么是全小写，要么是中划线写法，因为html不区分大小写，所以属性名会被转换为全小写(propertyName -> propertyname)
    2. 属性名如果是key的时候，key会被vue作为特殊属性在元素更新的时候使用，所以最终不会被渲染在元素的属性上
    3. 属性值因为使用了v-bind，所以如果绑定的是一个值，需要手动加上引号，否则会被判定为变量来进行解析
-->
<h2 :[name]="'propertyValue'">Hello World</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>绑定一个对象</code></p>
<p>如果我们希望将一个对象的所有属性，绑定到元素上的时候，可以直接绑定一个对象，vue在解析的时候会将对象展开后在进行传递，这对于传递props是十分有帮助的。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- <h2 name="Klaus" age="23">Hello World</h2> -->
<h2 v-bind="userInfo">Hello World</h2>

<!-- 简写 --- 语法糖 -->
<h2 :="userInfo">Hello World</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">v-on</h5>
<p>在前端开发中，我们需要经常和用户进行各种各样的交互</p>
<p>在Vue中如何监听事件 就需要使用v-on指令</p>
<pre><code class="hljs language-vue copyable" lang="vue"><button v-on:click="handleClick">click me</button>

<!-- 简写 -->
<button @click="handleClick">click me</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- v-on 的属性值可以是 function | inline statement | object -->

<!-- function -->
<button v-on:click="handleClick">click me</button>

<!-- inline statement -->
<button v-on:click="count++">&#123;&#123; count &#125;&#125;</button>

<!-- object --- 用于同时绑定多个事件 -->
<button v-on="&#123; click: handleClick, mouseup: handleMouseUp &#125;">click me</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>参数传递</code></p>
<pre><code class="hljs language-vue copyable" lang="vue"><!-- 如果函数没有任何的参数，那么vue会默认给事件处理函数一个参数，即事件对象event -->
<button v-on:click="handleClick">click me</button>

methods: &#123;
  handleClick(e) &#123;
    console.log(e)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue"><!--
  如果函数传递了参数，此时如果需要再获取事件参数对象的时候，需要自己手动传入$event
  $event 是vue封装好的特殊变量，表示的就是对应事件的事件处理函数
-->
<button v-on:click="handleClick('msg', $event)">click me</button>

methods: &#123;
    handleClick(msg, e) &#123;
      console.log(e, msg)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>事件修饰符</code></p>
<p>v-on支持修饰符，修饰符相当于对事件进行了一些特殊的处理</p>




























































<table><thead><tr><th>修饰符</th><th>作用</th><th>备注</th></tr></thead><tbody><tr><td>.stop</td><td>调用 event.stopPropagation()</td><td></td></tr><tr><td>.prevent</td><td>调用 event.preventDefault()</td><td></td></tr><tr><td>.capture</td><td>添加事件侦听器时使用 capture 模式</td><td></td></tr><tr><td>.self</td><td>只当事件是从侦听器绑定的元素本身触发时才触发回</td><td></td></tr><tr><td>.&#123;keyAlias&#125;</td><td>仅当事件是从特定键触发时才触发回调</td><td>keyAlias表示的是按键别名，<br>如enter，delete, tab, space ... 等</td></tr><tr><td>.once</td><td>只触发一次回调</td><td></td></tr><tr><td>.left</td><td>只当点击鼠标左键时触发</td><td></td></tr><tr><td>.right</td><td>只当点击鼠标右键时触发</td><td></td></tr><tr><td>.middle</td><td>只当点击鼠标中键时触发</td><td></td></tr><tr><td>.passive</td><td>&#123; passive: true &#125; 模式添加侦听器</td><td>表示在进行事件处理的时候，显示的告诉浏览器，<br>不会阻止默认事件，即不需要去检测是否有阻止默认行为<br>这对于一些会频繁调用多次的事件(如scroll， mousemove等)会有性能提升的效果</td></tr></tbody></table>
<pre><code class="hljs language-vue copyable" lang="vue"><div @click="handleDIVClick">
  <button @click.stop="handleBtnClick">click me</button>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">字符串模拟和DOM模板</h4>
<p><code>字符串模板</code></p>
<p>字符串模板就是写在vue中的template中定义的模板</p>
<ul>
<li>vue的单文件组件模板</li>
<li>定义组件时template属性值的模板(没有被抽取出去的时候)</li>
</ul>
<p>字符串模板不会在页面初始化参与页面的渲染，会被vue进行解析编译之后再被浏览器渲染，所以不受限于html不区分大小写的影响。</p>
<pre><code class="hljs language-vue copyable" lang="vue">Vue.component('Cpn', &#123;
   // MyComponent 定义在template中，会先经过vue的解析再渲染，所以其命名不受限于html不区分大小写的影响
   template: '<div MyId="123"><MyComponent>hello, world</MyComponent></div>'
&#125;)

<div id="app">
  <Cpn />
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dom模板</code></p>
<p>dom模板(又被称为Html模板）</p>
<p>dom模板就是写在html文件中，一打开就会被浏览器进行解析渲染的，即在经过vue解析之前就会先被浏览器所解析</p>
<p>因为html不区分大小写，所以此时类似于<code>myComponent</code>会被浏览器转换为<code>mycomponent</code>，此时在交给vue去进行解析的时候就会出现问题</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Vue Component<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span> 
      Hello Vue
      <span class="hljs-tag"><<span class="hljs-name">MyComponent</span>></span><span class="hljs-tag"></<span class="hljs-name">MyComponent</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.5.16/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> ></span><span class="javascript">
      <span class="hljs-comment">// MyComponent被解析为了mycomponent，所以vue找不到MyComponent这个组件，会报错</span>
      Vue.component(<span class="hljs-string">'MyComponent'</span>, &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>组件类容</div>'</span>
      &#125;);
      <span class="hljs-keyword">new</span> Vue (&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>
      &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此vue推荐在使用组件的时候，使用中划线的方式去使用（如my-component），而不是使用驼峰法(如MyComponent)的方式去使用。</p>
<h3 data-id="heading-10">扩展</h3>
<p>在html中有一些属性比较特别，它就是驼峰定义的（例如svg标签中的viewBox属性），所以以驼峰方式使用的时候不会有任何的问题</p>
<pre><code class="hljs language-vue copyable" lang="vue"><svg style="width:150px; height:300px" viewBox="0 0 400 400">
  <circle cx="200" cy="200" r="200" fill="#fdd" stroke="none"></circle>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是为了统一，有的时候，我们希望它和其它属性一样都使用中划线去进行定义，为了正常解析这类标签，vue提供了<code>camel</code>修饰符</p>
<p><code>.camel</code> 修饰符允许在使用<code> DOM 模板</code>时将 <code>v-bind</code> property 名称驼峰，</p>
<p>在使用<code>字符串模板</code>或通过 <code>vue-loader</code> 编译时，无需使用 <code>.camel</code>，因为此时vue会帮助我们处理好。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--
   :view-box.camel 会被编译为 viewBox
    ps: 使用camel修饰符的时候，必须是在v-bind的情况下， :view-box.camel ===> viewBox
    如果没有结合v-bind，会被解析为 view-box.camel ===> view-box.camel
--></span>
<span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width:150px; height:300px"</span> <span class="hljs-attr">:view-box.camel</span>=<span class="hljs-string">"'0 0 400 400'"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#fdd"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 
    camel修饰符如果用在原生不是驼峰的属性，
    :data-property.camel会被解析为dataproperty
    这是没有意义的
--></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:data-property.camel</span>=<span class="hljs-string">"'value'"</span>></span>Hello Vue<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            