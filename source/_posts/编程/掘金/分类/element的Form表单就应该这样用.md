
---
title: 'element的Form表单就应该这样用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6047'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 23:20:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=6047'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;position:relative;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;padding-left:8px;padding-bottom:0;margin-top:35px;margin-bottom:10px;font-weight:900;font-family:serif;letter-spacing:1px;color:#000&#125;.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover&#123;background-color:#fff&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;font-size:24px;position:relative&#125;.markdown-body h2:after&#123;content:"";left:0;bottom:0;width:100%;height:1px;position:absolute&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#37b2ff 0,#37b2ff 25%,transparent 50%)&#125;.markdown-body code&#123;margin:0 4px;word-break:break-word;overflow-x:auto;background-color:#fff7f7;color:#f06;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:-apple-system,system-ui,Menlo,Monaco,Consolas,Courier New;position:relative&#125;.markdown-body pre&#123;margin:15px 8px;border:1px solid #f5f5f7;line-height:1.75&#125;.markdown-body pre:before&#123;top:-4px;left:-4px;border-top:8px solid #feea1e;border-left:8px solid #feea1e&#125;.markdown-body pre:after,.markdown-body pre:before&#123;width:20px;height:20px;content:"";z-index:10;position:absolute&#125;.markdown-body pre:after&#123;right:-4px;bottom:-4px;border-right:8px solid #37b2ff;border-bottom:8px solid #37b2ff&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;overflow-x:auto;margin:0;word-break:normal;display:block;color:#333;background-color:#fff;background-image:linear-gradient(135deg,hsla(0,0%,87.8%,.1),hsla(0,0%,87.8%,.1) 25%,transparent 0,transparent 50%,hsla(0,0%,87.8%,.1) 0,hsla(0,0%,87.8%,.1) 75%,transparent 0,transparent)!important;background-size:10px 10px!important;position:unset!important&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#37b2ff;transition:.3s;border-bottom:1px dashed #37b2ff;position:relative;display:inline-block;vertical-align:bottom&#125;.markdown-body a:before&#123;bottom:90%;width:120px;max-width:0;content:"READ MORE +";color:#fff;background-color:#1fb3ff;position:absolute;white-space:nowrap;transition:.3s;box-sizing:border-box;pointer-events:none;overflow:hidden&#125;.markdown-body a:active:before,.markdown-body a:hover:before&#123;max-width:120px;padding-left:14px&#125;.markdown-body table&#123;width:100%;max-width:100%;font-size:12px;background-color:#fff;overflow:auto;border-collapse:collapse&#125;.markdown-body table tr:hover td,.markdown-body table tr:hover th&#123;border-bottom:1px solid #feea1e&#125;.markdown-body thead&#123;text-align:left&#125;.markdown-body th&#123;font-size:1.2em;border-bottom:1px dashed #eee&#125;.markdown-body tr:nth-child(2n)&#123;background-color:hsla(0,0%,87.8%,.1);border-bottom:1px solid #fff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px;border-bottom:1px dashed #fff&#125;.markdown-body blockquote&#123;color:#666;padding:12px 23px 2px;border:1px solid #37b2ff;background-color:#fff;margin:22px 0;position:relative&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body blockquote:after&#123;content:"FROM";left:0;width:40px;color:#fff;background-color:#37b2ff;text-align:center&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;top:0;line-height:1;padding:2px 0;font-size:12px;font-weight:lighter;position:absolute;pointer-events:none&#125;.markdown-body blockquote:before&#123;content:"CITATION";left:44px;color:#37b2ff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;line-height:2em;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol ol li,.markdown-body ol ul li,.markdown-body ul ol li,.markdown-body ul ul li&#123;border-bottom:none&#125;.markdown-body ol li&#123;padding-left:6px;list-style:decimal-leading-zero&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;.markdown-body input[type=checkbox i]:disabled&#123;background-color:#6cf&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<p>最近在做一系列后台管理系统，其中用的最多的就是表单和表格了。这里讲一下我最近对表单封装的思考。
以下是我的设计思路以及具体实现，我使用的是vue3+element-plus，因此这个组件也是以这两个库为基础。</p>
<h1 data-id="heading-0">设计目标</h1>
<h2 data-id="heading-1">配置化</h2>
<p>我们希望把表格的内容，验证规则,甚至于表单的样式，格式都能更规则化，配置化，这样后续我们可以通过构造json去实现一个表单，甚至可用实现拖拽式的构造表单。</p>
<h2 data-id="heading-2">参数简单</h2>
<p>尽量减少json的层级，减少json的参数，字段更加语义化。</p>
<h2 data-id="heading-3">自由度</h2>
<p>json其实是一套自由度的很少的规则，但是vue则我们提供更多的自由度，比如h函数，比如动态组件，利用这些方法我们可以实现更高的自由度。</p>
<h1 data-id="heading-4">我的实现过程</h1>
<h2 data-id="heading-5">表单项的格式设计</h2>
<p>首先第一步，我们先设计一个基础的格式,在这个JSON里，字段名都是很简单的英文单词，我专门把验证的规则rule放到每个子项里来，这也比较符合直观。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> oneItem = &#123;
          <span class="hljs-attr">key</span>: <span class="hljs-string">'title'</span>,
          <span class="hljs-attr">title</span>: <span class="hljs-string">'小说名'</span>,
          <span class="hljs-attr">component</span>: <span class="hljs-string">'el-input'</span>,
          <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">placeholder</span>: <span class="hljs-string">'请输入姓名'</span> &#125;,
          <span class="hljs-attr">rule</span>: [&#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'必填项'</span> &#125;],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个格式里面，比较重要的主要是2个，<code>key</code>，<code>component</code>。<code>key</code>其实就是你表单里数据的字段名，而<code>component</code>则是你指定的编辑组件，在这里我们可以直接使用字符串，但其实这里可以通过vue的动态组件实现更灵活的应用，比如我们换一个组件库的input组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Input</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@varlet/ui'</span> 
<span class="hljs-keyword">import</span> <span class="hljs-string">'@varlet/ui/es/input/style/index.js'</span>
<span class="hljs-keyword">const</span> oneItem = &#123;  <span class="hljs-attr">component</span>:  <span class="hljs-title class_">Input</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候，我们就需要动态组件去渲染它，因此我们可以这样写去渲染，当component是一个字符串，比如<code>el-input</code>的时候，我们渲染<code>element</code>的<code>input</code>组件，至于v-model这些我就省略了</p>
<pre><code class="hljs language-js copyable" lang="js"><el-form-item v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"item in items"</span> :key=<span class="hljs-string">"item.key"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.component === 'el-input'"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"item.component"</span> /></span></span>
</el-form-item>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">v-bind的妙用</h2>
<p>每个组件库的组件参数都不一样，而且有些属性我们可能并不使用，比如<code>el-input</code>有这个属性<code>prefix-icon</code>，是一个前缀图标,别的组件库不一定有啊，那到我们需要把所有组件库的所有属性都写在json？
我在之前的json中设计了以个<code>props</code>字段，这里面就是存放的是组件库的属性，或者是我们需要给组件传的值.
这时候，vue给我们提供了一个很方便的功能，直接使用<code>v-bind</code>传入一个对象，他就自动会帮我们把属性绑定。
比如这样写</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">props</span> = &#123;a:<span class="hljs-number">1</span>,b:<span class="hljs-number">2</span>&#125;
 <el-input <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.component === 'el-input'"</span> v-bind=<span class="hljs-string">"props"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue就会自动处理为下面这种, 这就是v-bind的妙用。当然运用<code>renderFunction</code>也可以实现这个效果，诸君可以自己尝试一下</p>
<pre><code class="hljs language-ini copyable" lang="ini"> <el-input <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.component === 'el-input'"</span> v-bind:a=<span class="hljs-string">"props.a"</span> v-bind:a=<span class="hljs-string">"props.b"</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">computed的妙用：实现v-model</h2>
<p>下面我们来看一下数据的问题，vue中提供了方便<code>v-model</code>，方便我们修改的值能实时响应,并且我们可以自己实现一自定义<code>v-model</code>。
它的基本原理是这样，我们先父传子，然后子再通过事件告诉父组件修改这个值。大概实现就是这样</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</script>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">props</span>:[
    <span class="hljs-string">'modelValue'</span>, <span class="hljs-comment">//v-model</span>
    <span class="hljs-string">'a'</span> <span class="hljs-comment">//v-model:a</span>
    ],

    <span class="hljs-attr">emits</span>:[<span class="hljs-string">'update:modelValue'</span>,<span class="hljs-string">'update:a'</span>],
  
    <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-title function_">add</span>(<span class="hljs-params"></span>)&#123;
            <span class="hljs-variable language_">this</span>.$emit(<span class="hljs-string">'update:modelValue'</span>,<span class="hljs-variable language_">this</span>.<span class="hljs-property">modelValue</span>++)
            <span class="hljs-variable language_">this</span>.$emit(<span class="hljs-string">'update:a'</span>,<span class="hljs-variable language_">this</span>.<span class="hljs-property">a</span>++)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这个代码里有一个问题，在vue中我们其实是无法修改props的，也就是说<code>this.modelValue++</code>会报错，那么如何解决这个问题呢，答案就是<code>computed</code>,<code>computed</code>其实也可以修改的，我们可以指定它的set方法,这样就躲避了修改props的问题，从而实现了<code>v-model</code></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">&#123;
    computed:&#123;
        num:&#123;
            <span class="hljs-keyword">get</span>()&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.modelValue
            &#125;,
            <span class="hljs-keyword">set</span>(<span class="hljs-keyword">val</span>)&#123;
                 <span class="hljs-keyword">this</span>.$emit(<span class="hljs-string">'update:modelValue'</span>,<span class="hljs-keyword">val</span>)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">useAttrs的妙用</h2>
<p>在我的组件中有这样一个功能，上传。这就涉及到了回调函数的问题，也就是说我上传完，甚至包括方法的名字，这样才更灵活，比如我们在json中新增一个字段，</p>
<pre><code class="hljs language-css copyable" lang="css">&#123;
 uploader: &#123;
     emits: <span class="hljs-string">'handleUploadCover'</span>,
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我在渲染的时候会给它绑上这个事件,那么我们如何获取到这个事件的函数，并调用呢？</p>
<pre><code class="hljs language-ini copyable" lang="ini"><zForm @<span class="hljs-attr">handleUploadCover</span>=<span class="hljs-string">"xxx"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中，我使用了useAttrs,需要注意的是vue3这里似乎与vue2有些不同。vue3中，attrs获取到的是没有注册的值，比如你如果在<code>emits</code>里声明了，在这里就取不到了，不过这也正合我意，我们可以随意指定事件名。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> attrs = <span class="hljs-title function_">useAttrs</span>()
<span class="hljs-comment">/*
  返回值
 &#123;
     onHandleUploadCover:function()&#123;xxx&#125;
 &#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这里能获取事件，只是名字略有不同，这里大家处理一下就行了</p>
<h2 data-id="heading-9">表单验证</h2>
<p>表单里最重要的就是验证.首先在我之前的设计中，表单验证的规则是分布在每一个子项中，因此我们需要整合一下，这一块我就不赘述了，也很简单。</p>
<p>验证方法我是直接使用的<code>el-form</code>的验证,只是封装了一下罢了。
需要注意的是，如果你用的是script setup，需要使用<code>defineExpose</code>导出这个方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> <span class="hljs-title function_">validate</span> = (<span class="hljs-params"></span>)=> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">$refs</span>.<span class="hljs-property">form</span>.<span class="hljs-title function_">validate</span>(<span class="hljs-function">(<span class="hljs-params">isValid</span>) =></span> <span class="hljs-title function_">resolve</span>(isValid));
      &#125;)
 <span class="hljs-title function_">defineExpose</span>(&#123;
     validate
 &#125;)     
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">上传文件</h2>
<p>上传文件这里我其实截取了一下element的上传，只使用了它选择的文件的功能，这块其实可以自己实现的。
因为我上传中间还要加很多参数，还有验证，因此我使用了<code>before-upload</code>方法，并主动reject.</p>
<pre><code class="hljs language-ini copyable" lang="ini"> <el-upload
        <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.uploader"</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-top: 10px"</span>
        :<span class="hljs-attr">before-upload</span>=<span class="hljs-string">"(file) => beforeUpload(file, item)"</span>
        :<span class="hljs-attr">show-file-list</span>=<span class="hljs-string">"false"</span>
        <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"item.uploader.props"</span>
      >
        <el-button <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>>点击上传</el-button>
 </el-upload>
 const <span class="hljs-attr">beforeUpload</span> = (rawFile, &#123; key, uploader &#125;) => &#123;
     /*执行逻辑，其实就是调起uploader.emits里的方法*/
     return Promise.reject()
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">代码总结</h1>
<p>我把demo放到了这里，后续有时间我整理一下发个npm包。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackblitz.com%2Fedit%2Fvue-m8veut%3Ffile%3Dsrc%2Fcomponents%2FZForm.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://stackblitz.com/edit/vue-m8veut?file=src/components/ZForm.vue" ref="nofollow noopener noreferrer">stackblitz.com/edit/vue-m8…</a></p>
<p>这次封装这个组件，我学到了很多东西，一些比较细微的vue3知识点，比如<code>v-bind</code>。但我也知道这也封装也有一些问题或者叫争论。</p>
<h2 data-id="heading-12">到底应不应该使用json</h2>
<p>之前看过一篇封装el-table的文章，里面就反对使用json，原因无非2点：json结构过于庞大，json结构不利于接手代码的人使用。</p>
<ul>
<li>先说第二点，我觉得通过我的定义是可以缓解这个问题的,但是难道你函数式封装就没有学习成本了？我觉得json封装其实每次就是赋值黏贴，反而学习成本更低，但是开发成本会更高，你需要处理错误的值，错误的结构，因此结构越简单越好，甚至可以拍平。</li>
<li>json结构并不庞大，庞大的是我们的表单，如果你表单里几百个条目，你怎么样写都只会庞大，因此还是建议分割表单，及时上报。</li>
</ul>
<h2 data-id="heading-13">需不需要v-model</h2>
<p>在我这次封装中，我把数据通过<code>v-model</code>实时返回了，但是当我写到结尾的时候，我觉得表单的数据并不需要实时，因为我们需要的不是当前的数据，而是验证后的正确数据。因此我觉得我们可以暴露出一个<code>getData</code>方法，返回验证正确的数据。</p>
<h2 data-id="heading-14">性能问题</h2>
<p>实际使用中，我发现这样封装似乎有点卡，目前暂时不知道是哪里的问题，有待研究</p></div>  
</div>
            