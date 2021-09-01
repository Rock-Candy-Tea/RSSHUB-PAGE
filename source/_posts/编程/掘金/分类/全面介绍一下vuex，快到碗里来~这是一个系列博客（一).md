
---
title: '全面介绍一下vuex，快到碗里来~这是一个系列博客（一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://tech.taiji.com.cn/ui/api/upload/0d17bc34f2304488afea3f122423b453.png'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 18:47:04 GMT
thumbnail: 'https://tech.taiji.com.cn/ui/api/upload/0d17bc34f2304488afea3f122423b453.png'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h5 data-id="heading-0">vuex是一个专门为vue.js设计的集中式状态管理架构。集中式存储和管理应用程序中所有组件的状态。Vuex 也集成到 Vue 的官方调试工具，一个 Vuex 应用的核心是 store（仓库，一个容器），store包含着你的应用中大部分的状态 (state)。</h5>
<p>什么是状态？
可以把它理解为在data中的属性需要共享给其他vue组件使用的部分，就叫做状态。简单的说就是data中需要共用的属性。比如：我们有几个页面要显示用户名称和用户等级，或者显示用户的地理位置。如果我们不把这些属性设置为状态，那每个页面遇到后，都会到服务器进行查找计算，返回后再显示。在中大型项目中会有很多共用的数据，所以尤大神给我们提供了vuex。</p>
<h3 data-id="heading-1">引入vuex</h3>
<h5 data-id="heading-2">1.利用npm包管理工具，进行安装 vuex。</h5>
<p>在控制命令行中输入下边的命令就可以了。
<code>cnpm install vuex --save</code>
<em>注意</em>：这里一定要加上 –save，因为你这个包我们在生产环境中是要有包的依赖。
添加完成后可以看到package.json中
<img src="https://tech.taiji.com.cn/ui/api/upload/0d17bc34f2304488afea3f122423b453.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">2.新建一个vuex文件夹（这个不是必须的）</h5>
<p>并在文件夹下新建store.js文件，文件中引入我们的vue和vuex。</p>
<h5 data-id="heading-4">3.使用我们vuex，引入之后用Vue.use进行引用。</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span>  <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;
Vue.use(Vuex);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这三步的操作，vuex就算引用成功了，接下来我们就可以尽情的使用了。
我们测试使用一下：
1.现在我们store.js文件里增加一个常量对象。store.js文件就是我们在引入vuex时的那个文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> state=&#123;
  <span class="hljs-attr">count</span>:<span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.用export default 封装代码，让外部可以引用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  state
)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.新建一个vue的模板，位置在components文件夹下，名字叫count.vue。在模板中我们引入我们刚建的store.js文件，并在模板中用&#123;&#123;$store.state.count&#125;&#125;输出count 的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span><span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123;$store.state.count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$store.commit('add')"</span>></span>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$store.commit('reduce')"</span>></span>reduce<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/vuex/store.js'</span>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"Count"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">msg</span>:<span class="hljs-string">'Hello Vuex'</span>
          &#125;
        &#125;,
        store
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.在store.js文件中加入两个改变state的方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> mutations=&#123;
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span>&#123;
    state.count ++;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">reduce</span>(<span class="hljs-params">state</span>)</span>&#123;
    state.count--;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的mutations是固定的写法，意思是改变的，我们后面会专门分享这个mutations，所以你先不用着急，只知道我们要改变state的数值的方法，必须写在mutations里就可以了。
5.在count.vue模板中加入两个按钮，并调用mutations中的方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <p>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$store.commit('add')"</span>></span>add<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$store.commit('reduce')"</span>></span>reduce<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样进行预览就可以实现对vuex中的count进行加减了。</p>
<h3 data-id="heading-5">vuex state访问状态对象</h3>
<h5 data-id="heading-6">前面章节我们写了一个const state ，这个就是我们说的访问状态对象，它就是SPA（单页应用程序）中的共享值。今天主要学习状态对象赋值给内部对象，也就是把stores.js中的值，赋值给我们模板里data中的值。有三种赋值方式。下面介绍一下这三种方式并进行测试。</h5>
<h4 data-id="heading-7">1.通过computed的计算属性直接赋值</h4>
<p>computed属性可以在输出前，对data中的值进行改变，我们就利用这种特性把store.js中的state值赋值给模板中的data值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed:&#123;
  <span class="hljs-function"><span class="hljs-title">count</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.count;
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是return this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi><mi>t</mi><mi>o</mi><mi>r</mi><mi>e</mi><mi mathvariant="normal">.</mi><mi>s</mi><mi>t</mi><mi>a</mi><mi>t</mi><mi>e</mi><mi mathvariant="normal">.</mi><mi>c</mi><mi>o</mi><mi>u</mi><mi>n</mi><mi>t</mi><mtext>这一句，一定要写</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mtext>，要不你会找不到</mtext></mrow><annotation encoding="application/x-tex">store.state.count这一句，一定要写this，要不你会找不到</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord">.</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord">.</span><span class="mord mathnormal">c</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">这</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">句</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">定</span><span class="mord cjk_fallback">要</span><span class="mord cjk_fallback">写</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">要</span><span class="mord cjk_fallback">不</span><span class="mord cjk_fallback">你</span><span class="mord cjk_fallback">会</span><span class="mord cjk_fallback">找</span><span class="mord cjk_fallback">不</span><span class="mord cjk_fallback">到</span></span></span></span></span>store的。这种写法很好理解，但是写起来是比较麻烦的，那我们来看看第二种写法。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123;$store.state.count&#125;&#125;-&#123;&#123;count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2.通过 mapState的对象来赋值</h4>
<p>首先要引入mapState，这块有个小坑，mapState一定要加&#123;&#125;
<code>import &#123;mapState&#125; from 'vuex';</code>
然后还在computed计算属性里写如下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed:mapState(&#123;
  <span class="hljs-attr">count</span>:<span class="hljs-function"><span class="hljs-params">state</span>=></span>state.count
&#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">3.通过mapState的数组来赋值</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed:mapState([<span class="hljs-string">"count"</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个算是最简单的写法了，在实际项目开发当中也经常这样使用。</p>
<p><em><strong>这是关于VUEX的系列博客，持续更新中~</strong></em></p>
<p><strong>前端路漫漫其修远兮，吾将上下而求索，一起加油，学习前端吧~</strong> *<strong>我是圈圈，看我沸点可以入群~</strong></p></div>  
</div>
            