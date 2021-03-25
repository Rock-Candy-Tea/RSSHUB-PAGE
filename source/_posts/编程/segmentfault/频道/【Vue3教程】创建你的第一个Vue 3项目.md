
---
title: '【Vue3教程】创建你的第一个Vue 3项目'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/bVcQEXO'
author: segmentfault
comments: false
date: 2021-03-25 00:36:55
thumbnail: 'https://segmentfault.com/img/bVcQEXO'
---

<div>   
<blockquote>作者：Shadeed<br>译者：前端小智<br>来源：dmitripavlutin</blockquote><blockquote><strong>点赞再看</strong>，微信搜索<strong>【<a href="https://mp.weixin.qq.com/s/sY9ufGGKfcdaAQ7KJQs3HA" rel="nofollow">大迁世界</a>】</strong>,B站关注<strong>【<a href="https://space.bilibili.com/31089477" rel="nofollow">前端小智</a>】</strong>这个没有大厂背景，但有着一股向上积极心态人。本文 <code>GitHub</code> <a href="https://github.com/qq449245884/xiaozhi" rel="nofollow">https://github.com/qq44924588...</a> 上已经收录，文章的已分类，也整理了很多我的文档，和教程资料。</blockquote><p>最近开源了一个 Vue 组件，还不够完善，欢迎大家来一起完善它，也希望大家能给个 star 支持一下，谢谢各位了。</p><p><strong>github 地址：<a href="https://github.com/qq449245884/vue-okr-tree" rel="nofollow">https://github.com/qq44924588...</a></strong></p><p>2021年2月15日Vue 3正式发布!在<strong>尤雨溪</strong>的声明中，他宣布了新框架中最大的变化，并谈论了整个Vue团队所做的出色工作。</p><p>长期以来，开发者一直在等待Vue 3宣布的真正酷的特性，比如Typescript支持、对大型项目更好的组织、及使Vue应用程序更好的渲染优化。</p><p>本文中我们要做以下的内容，使用组合API构建了两个组件。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEXO" alt="image" title="image" referrerpolicy="no-referrer"></span></p><h3>开始</h3><p>有几种不同的选项可用于将Vue 3添加到现有项目或创建自己的Vue 3项目。</p><p>这里，我用自己最喜欢的两个选项：</p><ol><li>Vue CLI</li><li>Vite</li></ol><h3>Vue CLI</h3><p>如果你用过Vue开发，那么很可能使用了<strong>Vue CLI</strong>来设置项目。</p><p>首先，我们必须确保拥有Vue CLI的最新版本，可以通过在终端上运行 <code>npm update -g @vue/cli</code> 来做到这一点。</p><p>接下来，创建项目，运行 <code>vue create <项目名></code>，如果 CLI是最新的，我们就可以选择Vue 3。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEYT" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>选择了Vue 3选项，我们的应用程序便会构建。 完成后，我们只需要进入我们的项目，然后运行我们的Vue应用, 该命令是：</p><pre><code>cd <项目我>
npm run serve</code></pre><p>现在，在浏览器中输入<code>http://localhost:8080/</code>，就会看到我们的应用程序！</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEYY" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h3>Vite</h3><p>Vite (法语意为 "快速的"，发音 <code>/vit/</code>) 是一种新型前端构建工具，能够显著提升前端开发体验，它主要由两部分组成：</p><ul><li>一个开发服务器，它利用 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules" rel="nofollow">原生 ES 模块</a> 提供了 <a href="https://www.pipipi.net/vite/guide/features.html" rel="nofollow">丰富的内建功能</a>，如速度快到惊人的 <a href="https://www.pipipi.net/vite/guide/features.html#hot-module-replacement" rel="nofollow">模块热更新（HMR）</a>。</li><li>一套构建指令，它使用 <a href="https://rollupjs.org/" rel="nofollow">Rollup</a> 打包你的代码，预配置输出高度优化的静态资源用于生产。</li></ul><h4>为什么使用 Vite</h4><p>你现在可能会有疑问？，那么 <code>Vite</code> 与现有的<code> vue-cli</code>到底有什么不同呢?</p><p>由于@ vue-cli / service是在webpack之上构建的，因此它是一个模块捆绑程序，它将在启动，热重载和编译时捆绑整个Vue项目。</p><p>由于<code>@vue-cli/service</code>是在webpack之上构建的，因此它是一个模块捆绑程序，它将在启动，热重载和编译时捆绑整个Vue项目。</p><p>Webpack 的工作方式是，它通过解析应用程序中的每一个 <code>import</code> 和 <code>require</code> ，将整个应用程序构建成一个基于 JavaScript 的捆绑包，并在运行时转换文件（例如 Sass、TypeScript、SFC）。</p><p>这都是在服务器端完成的，依赖的数量和改变后构建/重新构建的时间之间有一个大致的线性关系。</p><p>相反，Vite 不捆绑应用服务器端。相反，它依赖于浏览器对 JavaScript 模块的原生支持（也就是 ES 模块，是一个比较新的功能）。</p><p>浏览器将在需要时通过 HTTP 请求任何 JS 模块，并在运行时进行处理。Vite 开发服务器将按需转换任何文件（如 Sass、TypeScript、SFC）。</p><p>这种架构避免了服务器端对整个应用的捆绑，并利用浏览器高效的模块处理，提供了一个明显更快的开发服务器。</p><blockquote>提示：当你对应用程序进行 code-split 和 tree-shake 动时，Vite 的速度会更快，因为它只加载它需要的模块，即使是在开发阶段。这与 Webpack 不同，在 Webpack 中，代码拆分只对生产包有利。</blockquote><h4>创建第一个Vite项目</h4><p>运行下面命令即可：</p><pre><code>npm init vite-app <项目名></code></pre><p>然后，我们只需进入我们的项目文件夹，安装依赖项，然后使用以下命令运行我们的应用程序:</p><pre><code>cd <项目名>
npm install
npm run dev</code></pre><p>现在，如果我们导航到<code>http://localhost:3000</code> –我们应该看到以下应用程序：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEZF" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h4>一些你应该知道的Vue Vite特性</h4><p><strong>1.将项目打包到生产中</strong></p><p>Vite的一个目标是使Vue的开发和生产尽可能容易。虽然在开发过程中没有捆绑，但是将你的项目捆绑到生产中是非常容易的。</p><p>你所要做的就是运行<code>npm run build</code>。</p><p>如果查看<code>package.json</code>，实现是运行 <code>vite build</code> –与其他构建过程一样，打包后会放在<code>dist</code>文件中。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEZN" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p><strong>2.asset 路径</strong></p><p>与其他Vue项目设置一样，Vite 提供了两种引用<code>asset</code>`的方法。</p><ol><li>绝对路径 - 使用公用文件夹。 这些资源使用<code>/file.extension</code>引用，并且在构建项目时将复制到<code>dist</code>文件夹的根目录中。</li><li>相对路径 - 例如，根据文件夹的文件结构来相对访问<code>src/assets</code>文件夹中的文件。 构建项目时，整个文件夹都将作为<code>_assets</code>放置在<code>dist</code>文件夹中。</li></ol><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEZ0" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p><strong>3.内置 Typescript 支持</strong></p><p>Vue3 最大的变化之一是使用Typescript重写了核心库，允许根据IDE进行类型检查和更好的错误消息。</p><p>通过提供对<code>.ts</code>文件和SFC中的<code><script lang =“ ts”></code>的内置Typescript支持，Vite再次与Vue 3顺利集成。</p><h3>理解 Vue3 组件</h3><p>现在我们已经设置好了Vue 3应用程序，并且理解了Vue 3 Vite工具，让我们来看看这些组件是如何工作的。</p><p>Vue 3中最大的变化是引入了组合API。在这个新的结构中，我们能够根据特性来组织代码，而不是仅仅通过<code>data</code>、<code>computed</code>等来分离代码。</p><p>这允许我们创建更多模块化、可读性和可伸缩性的代码，因为单个特性的代码都可以在代码的一个区域中编写。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVbG3Nz" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>如果打开<code>src/components/HelloWorld.vue</code>文件，我们将看到与我们在Vue2中编写的代码看起来相同的代码-这称为<strong>Options API</strong>。</p><pre><code><script>
export default &#123;
  name: 'HelloWorld',
  props: &#123;
    msg: String
  &#125;,
  data() &#123;
    return &#123;
      count: 0
    &#125;
  &#125;
&#125;
</script></code></pre><p>这很棒，因为在 Vue3 中，我们仍然可以在其中使用 vue2 的语法。</p><p>在本教程中，我们将介绍如何在新的<strong>Composition API</strong>中实现这一点，并从Options API中识别出这些变化。</p><h3>组合API中的响应性数据</h3><p>我们首先从vue核心库导入一些东西，以允许我们创建响应式变量。</p><pre><code>import &#123; ref &#125; from 'vue'</code></pre><p>然后，让我们用如下所示的<code>setup</code>函数替换<code>data</code>选项。</p><pre><code>import &#123; ref &#125; from 'vue'
  export default &#123;
    setup () &#123;
      
      return &#123;
       
      &#125;
    &#125;
  &#125;</code></pre><p>这个 <code>setup</code> 方法在组件创建时运行，在这里我们可以定义所有需要组件使用的响应数据、计算属性、方法等。</p><p>还有，该<code>setup</code>方法返回的任何内容都可以在模板中访问。</p><h4>使用 ref 创建响应式数据</h4><p>为了显示这一点，我们在模板中使用<code>v-model</code>创建一个文本输入。</p><pre><code><template>
   <div>
     <h2> Filter LearnVue Articles </h2>
     <input 
      type='text' 
      placeholder='Filter Search' 
      v-model='query'
    />
    &#123;&#123; query &#125;&#125;
   </div>
</template></code></pre><p>我们使用<code>ref</code>创建响应式<code>query</code>变量，然后从<code>setup</code>方法返回它。</p><pre><code>setup () &#123;
      const query = ref('')

      return &#123;
        query
      &#125;
&#125;</code></pre><p>然后，如返回到应用程序，会看到我们使用Composition API获得了响应式数据。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQE0O" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>很好！接下来，我们在<code>input</code>中添加一个<code>clear</code>按钮，看看如何在<strong>Composition API</strong>中创建一个方法。</p><h3>组合API中的方法</h3><p>在<strong>选项 API</strong>中，Vue对象中有一个完整的属性专门用于方法。对于较大的文件，这意味着数据可能在数百行之外的方法中声明，这使得组件更难读取和维护。</p><p>在<strong>组合API</strong>中，一切都在 <code>setup</code> 方法中，这意味着我们可以根据特性组织代码，甚至将通用特性提取到它们自己的代码模块中。</p><p>我们创建一个<code>reset</code>方法，它获取我们的<code>ref</code>并将其设置为一个空字符串。</p><pre><code>setup () &#123;
      const query = ref('')

      const reset = (evt) => &#123;
        query.value = '' // clears the query
      &#125;
      
      return &#123;
        reset,
        query
      &#125;
&#125;</code></pre><p>需要注意的一件事是，我们需要调用<code>query.value</code>才能访问数据的值。</p><p><strong>为什么？</strong></p><p>如果我们使用<code>console.log(query)</code>，我们看到它不仅仅是一个字符串值，而是一个 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy" rel="nofollow">Proxy</a>。使用 Proxy 允许我们轻松地获取数据变化，这也是为什么我们需要在引用上调用<code>.value</code>的原因。</p><p>然后，就像在<strong>选项API</strong>使用的一样，我们可以在模板中添加一个按钮，在单击时调用这个<code>reset</code>方法。</p><pre><code><button @click='reset'> Reset </button></code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQE1u" alt="image" title="image" referrerpolicy="no-referrer"></span></p><h3>向 Vue3 项目添加第二个组件</h3><p>现在我们已经有了输入和查询数据，接着，创建一个组件显示结果。</p><p>这个组件取名为<code>SearchResults.vue</code></p><p>要将其添加到我们的<code>HelloWorld.vue</code>组件中，首先必须将其导入并在我们的导出默认值中声明它。</p><pre><code><script>
  import &#123; ref &#125; from 'vue'
  import SearchResults from './SearchResults.vue'
  export default &#123;
    components: &#123;
      SearchResults
    &#125;,
    // ...
  &#125;
</script></code></pre><p>然后，我们可以像这样将它添加到模板中:</p><pre><code>// HelloWorld.vue
<template>
   <div>
     <h2> Filter LearnVue Articles </h2>
     <input 
      type='text' 
      placeholder='Filter Search' 
      v-model='query'
    />
    <br>
    <button @click='reset'> Reset </button>
    <search-results/>
   </div>
</template></code></pre><h3>传递参数</h3><p>Vue props 允许父组件将数据传递给其子组件。对于我们的例子，我们希望从<code>HelloWorld.vue</code>传递<code>query </code>字符串给<code>SearchResults.vue</code>。</p><pre><code>// HelloWorld.vue
<search-results :query='query'/></code></pre><h3>访问参数</h3><p>在<code>SearchResults.vue</code>内部，从 JSON 文件导入所有的文章信息。</p><pre><code>import titles from '../post-data.json'
export default &#123;
  setup (props, context) &#123;
 
  &#125;
&#125;</code></pre><p>然后，我们需要几个步骤来访问 <code>props</code>。</p><p>首先，我们必须在 <code>props</code> 选项中声明它们。这告诉我们的组件需要什么数据。</p><pre><code>// SearchResults.vue
export default &#123;
  props: &#123;
    query: String
  &#125;,
  setup (props, context) &#123;
  // ...</code></pre><p>如果我们仔细观察<code>setup</code>方法，就会发现它接受两个参数。</p><ol><li><code>props</code> – 包含传递给组件的所有 props</li><li><code>context</code>– 包含 <code>attrs</code>，<code>slot</code>和<code>emit</code></li></ol><p>我们将使用 <code>props</code> 在 <code>setup</code> 方法中访问我们的 <code>props</code> 的值。</p><p>我们所需要做的就是使用计算属性来过滤使文章列表。</p><h4>计算属性</h4><pre><code>// SearchResults.vue
import &#123; computed &#125; from 'vue'</code></pre><p>然后，我们这样设置它，其中我们的<code>computed</code>属性接受一个<code>getter</code>方法。每当其中一个依赖项发生更改时，此方法将更新我们的<code>computed</code>属性。</p><pre><code>// SearchResults.vue
import &#123; computed &#125; from 'vue'
import titles from '../post-data.json'
export default &#123;
  props: &#123;
    query: String
  &#125;,
  setup (props, context) &#123;
    
    const filteredTitles = computed(() => &#123;
     
    &#125;)

    return &#123;
      filteredTitles
    &#125;
  &#125;
&#125;</code></pre><p>对于这个方法，我们希望使用<code>query</code>过滤所有的标题。所有内容都转换为小写，所以我们不必担心大小写。</p><pre><code>// SearchResults.vue
const filteredTitles = computed(() => &#123;
      return titles.filter(s => s.Name.toLowerCase().includes(props.query.toLowerCase()))
    &#125;)</code></pre><p>很好~</p><p>剩下要做的就是实际使用我们的模板来显示数据!这是使用<code>v-for</code>循环完成的。</p><pre><code>// SearchResults.vue
<template>
  <div class='root'>
    <p> Showing &#123;&#123; filteredTitles.length &#125;&#125; results for "&#123;&#123; query &#125;&#125;" </p>
    <ul>
      <li v-for='title in filteredTitles' :key='title.Page'>
        &#123;&#123; title.Name &#125;&#125;
      </li>
    </ul>
  </div>
</template></code></pre><p>就这~</p><p>![上传中...]()</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQEXO" alt="image" title="image" referrerpolicy="no-referrer"></span></p><h3>Vue3 生命周期钩子</h3><p>在开始使用 Vue3 之前，还需要知道的另一件事是如何使用Vue<a href="https://learnvue.co/2020/03/how-to-use-lifecycle-hooks-in-vue3/" rel="nofollow">生命周期钩子</a>。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQE19" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>像Composition API的其他部分一样，我们必须导入我们想要使用的生命周期钩子，并在<code>setup</code>方法中声明它们。</p><pre><code>// Lifecycle Example 
import &#123; computed, onMounted &#125; from 'vue'
export default &#123;
  setup () &#123;
    
    onMounted(() => &#123;
      console.log('mounted')
    &#125;)
  &#125;
&#125;</code></pre><h3>总结</h3><p>Vue 3中有很多很棒的功能，这些功能对于创建可扩展的Vue应用程序非常有用。</p><p>希望本文本对你在使用 vue3 时提供一些帮助。</p><p>完~，我是刷碗智，我要去刷碗了，我们下期见~</p><hr><p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://www.fundebug.com/?utm_source=xiaozhi" rel="nofollow">Fundebug</a>。</strong></p><p>原文：<a href="https://learnue.co/2020/12/setting-up-your-frst-vue3-project-vue-3-0-release/" rel="nofollow">https://learnue.co/2020/12/se...</a></p><h2>交流</h2><p>文章每周持续更新，可以微信搜索「 大迁世界 」第一时间阅读和催更（比博客早一到两篇哟），本文 GitHub <a href="https://github.com/qq449245884/xiaozhi" rel="nofollow">https://github.com/qq449245884/xiaozhi</a>  已经收录，整理了很多我的文档，欢迎Star和完善，大家面试可以参照考点复习，另外关注公众号，后台回复<strong>福利</strong>，即可看到福利，你懂的。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000020353567?w=800&h=400" alt title referrerpolicy="no-referrer"></span></p>  
</div>
            