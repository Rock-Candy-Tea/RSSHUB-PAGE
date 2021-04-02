
---
title: '搞明白activated和deactivated'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b162f231879c465a98be4d20fa1fb12b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:44:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b162f231879c465a98be4d20fa1fb12b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文章目录</h3>
<ul>
<li>
<ul>
<li>
<ul>
<li>
<ul>
<li><a href="https://juejin.cn/post/6943478943362056222#_1">写到前面</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#activated_3">什么是activated</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#activated_5">activated解决了一个什么问题</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#Demo_7">Demo</a></li>
<li>
<ul>
<li><a href="https://juejin.cn/post/6943478943362056222#mainvue_8">main.vue</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#assembly11_54">assembly1(组件1)</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#assembly22_88">assembly2(组件2)</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6943478943362056222#_122">执行结果</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#_127">要点速记</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#_132">个人建议</a></li>
<li><a href="https://juejin.cn/post/6943478943362056222#_134">写到最后</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-1"><a href="https://juejin.cn/post/6943478943362056222"></a>写到前面</h4>
<blockquote>
<p>今天简单的将activated讲一下，前面有人问了，既然有问的，说明还有人不是很明白的，这里就说一下吧！</p>
</blockquote>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943478943362056222"></a>什么是activated</h4>
<blockquote>
<p>首先要确定一个点就是他也是属于vue生命周期中的一个，为什么我们平常说的生命周期没有它呢？我们平常说的生命周期就是created，update，mounted，destory和他们的之前之后的状态，当我们去查的activated的时候发现没有，但是会在官方的keep-alive中发现他的身影和介绍，知道你们不想找，<a href="https://cn.vuejs.org/v2/api/#keep-alive" target="_blank" rel="nofollow noopener noreferrer">点击它吧</a>，说白了就是我们直接切换组件的时候，组件的钩子函数会对应的触发，比如进来的时候出现created，离开的时候出现destory这样的，那么当我们使用缓存的时候，也就是keep-alive的时候，我们正常的钩子函数就没办法执行了，这个时候activated和deactivated就会执行。</p>
</blockquote>
<h4 data-id="heading-3"><a href="https://juejin.cn/post/6943478943362056222"></a>activated解决了一个什么问题</h4>
<blockquote>
<p>既然在文档上给他一席之地，说明他肯定是由自己存在的必要的，我们假设一种情况，我们做一个项目的时候，一个功能是引用了组件中的数据，这个时候我们需要每次进去的时候都最新的值给传递过去，更新掉，我们有几种办法，目前是三种，第一种是我们直接将数据作为参数，进行父子数据的传递，第二种办法是使用vuex状态管理这个值，进行全局一个状态管理，也是可以实现的，第三种就是我们将组件缓存，使用keep-alive，但是数据传递过去不会更新，因为created和mounted不执行，怎么办呢？这个时候就可以使用我们的activated进行更新我们的数据！</p>
</blockquote>
<h4 data-id="heading-4"><a href="https://juejin.cn/post/6943478943362056222"></a>Demo</h4>
<h5 data-id="heading-5"><a href="https://juejin.cn/post/6943478943362056222"></a>main.vue</h5>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <button @click="currAssembly('one')">
      组件1
    </button>
    <button @click="currAssembly('two')">
      组件2
    </button>
    <transition>
      <keep-alive>
        <component :is="isCurr"></component>
      </keep-alive>
    </transition>
  </div>
</template>

<script>
  import AssemblyOne from '../components/assembly1.vue'
  import AssemblyTwo from '../components/assembly2.vue'

  export default &#123;
    components: &#123;
      AssemblyOne,
      AssemblyTwo
    &#125;,
    data() &#123;
      return &#123;
        isCurr: 'AssemblyOne'
      &#125;
    &#125;,
    methods: &#123;
      currAssembly(flg) &#123;
        if (flg === 'one') &#123;
          this.isCurr = 'AssemblyOne'
        &#125; else &#123;
          this.isCurr = 'AssemblyTwo'
        &#125;
      &#125;
    &#125;
  &#125;
</script>
<style>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6"><a href="https://juejin.cn/post/6943478943362056222"></a>assembly1(组件1)</h5>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <h2>
      &#123;&#123;msg&#125;&#125;
    </h2>
  </div>
</template>

<script>
  export default &#123;
    data() &#123;
      return &#123;
        msg: 'this is assembly One'
      &#125;
    &#125;,
    created() &#123;
      console.info('我是组件1，此时我的created钩子已经被执行了')
    &#125;,
    mounted() &#123;
      console.info('我是组件1，此时我的mounted钩子已经被执行了')
    &#125;,
    activated() &#123;
      console.info('我是组件1，此时我的activated钩子已经被执行了')
    &#125;,
    deactivated() &#123;
      console.info('我是组件1，此时我的deactivated钩子已经被执行了')
    &#125;
  &#125;
</script>
<style>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7"><a href="https://juejin.cn/post/6943478943362056222"></a>assembly2(组件2)</h5>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <h2>
      &#123;&#123;msg&#125;&#125;
    </h2>
  </div>
</template>

<script>
  export default &#123;
    data() &#123;
      return &#123;
        msg: 'this is assembly Two'
      &#125;
    &#125;,
    created() &#123;
      console.info('我是组件2，此时我的created钩子已经被执行了')
    &#125;,
    mounted() &#123;
      console.info('我是组件2，此时我的mounted钩子已经被执行了')
    &#125;,
    activated() &#123;
      console.info('我是组件2，此时我的activated钩子已经被执行了')
    &#125;,
    deactivated() &#123;
      console.info('我是组件2，此时我的deactivated钩子已经被执行了')
    &#125;
  &#125;
</script>
<style>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8"><a href="https://juejin.cn/post/6943478943362056222"></a>执行结果</h4>
<ul>
<li>第一次运行<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b162f231879c465a98be4d20fa1fb12b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>第二次运行<br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10b999c49ea74ae2b7bb46d6dbb3aa16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<h4 data-id="heading-9"><a href="https://juejin.cn/post/6943478943362056222"></a>要点速记</h4>
<ul>
<li>activated和deactivated是配合keep-alive一起使用的</li>
<li>activated和deactivated没有keep-alive的时候是不会被触发的</li>
<li>在存在keep-alive的时候可以将activated当作created进行使用</li>
<li>deactivated是组件销毁的时候触发，此时的destory是不执行的</li>
</ul>
<h4 data-id="heading-10"><a href="https://juejin.cn/post/6943478943362056222"></a>个人建议</h4>
<p>将上面的几种情况自己模拟看一下，就会明白了！</p>
<h4 data-id="heading-11"><a href="https://juejin.cn/post/6943478943362056222"></a>写到最后</h4>
<blockquote>
<p>相信这个例子你们应该可以直接明白怎么回事了，我也不废话了，这个东西我想了一下要不要写一篇文章出来，但是呢，我觉得我之前想的都是错的，我一直认为只要是我个人觉得很简单的，我觉得你们都会了，所以很多时候我都不会去写博客，后来发现很多东西可能我遇到了你们没有遇到，让我觉得你们也遇到过，所以这个误会直接导致我很少更新博客了，以后尽量更新多一些内容。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            