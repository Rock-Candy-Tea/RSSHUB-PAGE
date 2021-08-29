
---
title: 'Vuex中的模块化-Module'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8214'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 17:37:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=8214'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">为什么会有模块化？</h3>
<blockquote>
<p>由于使用单一状态树，应用的所有状态会集中到一个比较大的对象。当应用变得非常复杂时，store 对象就有可能变得相当臃肿。</p>
</blockquote>
<p>这句话的意思是，如果把所有的状态都放在state中，当项目变得越来越大的时候，Vuex会变得越来越难以维护</p>
<p>由此，又有了Vuex的模块化</p>
<h3 data-id="heading-1">模块化的简单应用</h3>
<p><strong>应用</strong></p>
<p>定义两个模块   <strong>user</strong> 和  <strong>setting</strong></p>
<p>user中管理用户的状态  token</p>
<p>setting中管理 应用的名称 name</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store  = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">modules</span>: &#123;
    <span class="hljs-attr">user</span>: &#123;
       <span class="hljs-attr">state</span>: &#123;
         <span class="hljs-attr">token</span>: <span class="hljs-string">'12345'</span>
       &#125;
    &#125;,
    <span class="hljs-attr">setting</span>: &#123;
      <span class="hljs-attr">state</span>: &#123;
         <span class="hljs-attr">name</span>: <span class="hljs-string">'Vuex实例'</span>
      &#125;
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义child-b组件，分别显示用户的token和应用名称name</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
      <div>用户token &#123;&#123; $store.state.user.token &#125;&#125;</div>
      <div>网站名称 &#123;&#123; $store.state.setting.name &#125;&#125;</div>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意： 此时要获取子模块的状态 需要通过 $store.<strong><code>state</code></strong>.<strong><code>模块名称</code></strong>.<strong><code>属性名</code></strong> 来获取</p>
<blockquote>
<p>看着获取有点麻烦，我们可以通过之前学过的getters来改变一下</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> getters: &#123;
   <span class="hljs-attr">token</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.user.token,
   <span class="hljs-attr">name</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.setting.name
 &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意：这个getters是根级别的getters哦</p>
<p><strong>通过mapGetters引用</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> computed: &#123;
       ...mapGetters([<span class="hljs-string">'token'</span>, <span class="hljs-string">'name'</span>])
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">模块化中的命名空间</h3>
<p><strong>命名空间</strong>  <strong><code>namespaced</code></strong></p>
<blockquote>
<p>这里注意理解</p>
</blockquote>
<p>默认情况下，模块内部的 action、mutation 和 getter 是注册在<strong>全局命名空间</strong>的——这样使得多个模块能够对同一 mutation 或 action 作出响应。</p>
<blockquote>
<p>这句话的意思是 刚才的user模块还是setting模块，它的 action、mutation 和 getter 其实并没有区分，都可以直接通过全局的方式调用 如</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  user: &#123;
       <span class="hljs-attr">state</span>: &#123;
         <span class="hljs-attr">token</span>: <span class="hljs-string">'12345'</span>
       &#125;,
       <span class="hljs-attr">mutations</span>: &#123;
        <span class="hljs-comment">//  这里的state表示的是user的state</span>
         updateToken (state) &#123;
            state.token = <span class="hljs-number">678910</span>
         &#125;
       &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过mapMutations调用</strong></p>
<pre><code class="hljs language-vue copyable" lang="vue"> methods: &#123;
       ...mapMutations(['updateToken'])
  &#125;
 <button @click="updateToken">修改token</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>但是，如果我们想保证内部模块的高封闭性，我们可以采用namespaced来进行设置</p>
</blockquote>
<p>高封闭性？可以理解成 <strong>一家人如果分家了，此时，你的爸妈可以随意的进出分给你的小家，你觉得自己没什么隐私了，我们可以给自己的房门加一道锁（命名空间 namespaced）,你的父母再也不能进出你的小家了</strong></p>
<p>如</p>
<pre><code class="hljs language-js copyable" lang="js">  user: &#123;
       <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
       <span class="hljs-attr">state</span>: &#123;
         <span class="hljs-attr">token</span>: <span class="hljs-string">'12345'</span>
       &#125;,
       <span class="hljs-attr">mutations</span>: &#123;
        <span class="hljs-comment">//  这里的state表示的是user的state</span>
         updateToken (state) &#123;
            state.token = <span class="hljs-number">678910</span>
         &#125;
       &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用带命名空间的模块 <strong><code>action/mutations</code></strong></p>
<p>方案1：<strong>直接调用-带上模块的属性名路径</strong></p>
<pre><code class="hljs language-js copyable" lang="js">test () &#123;
   <span class="hljs-built_in">this</span>.$store.dispatch(<span class="hljs-string">'user/updateToken'</span>) <span class="hljs-comment">// 直接调用方法</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案2：<strong>辅助函数-带上模块的属性名路径</strong></p>
<pre><code class="hljs language-vue copyable" lang="vue">  methods: &#123;
       ...mapMutations(['user/updateToken']),
       test () &#123;
           this['user/updateToken']()
       &#125;
   &#125;
  <button @click="test">修改token</button>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案3： <strong>createNamespacedHelpers</strong>  创建基于某个命名空间辅助函数</p>
<pre><code class="hljs language-vue copyable" lang="vue">import &#123; mapGetters, createNamespacedHelpers &#125; from 'vuex'
const &#123; mapMutations &#125; = createNamespacedHelpers('user')
<button @click="updateToken">修改token2</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3"><strong>小结：</strong></h2>
<p>若有不懂的地方，请加q群147936127交流或者vx:  ltby52119，谢谢~</p></div>  
</div>
            