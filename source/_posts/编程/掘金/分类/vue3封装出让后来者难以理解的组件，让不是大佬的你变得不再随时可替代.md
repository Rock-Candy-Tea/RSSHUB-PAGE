
---
title: 'vue3封装出让后来者难以理解的组件，让不是大佬的你变得不再随时可替代'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f92d1cf08d4dc79b2cd6558cf01be9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 19:42:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f92d1cf08d4dc79b2cd6558cf01be9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f92d1cf08d4dc79b2cd6558cf01be9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>害，最近两个月忙于工作和生活（明明就是给自己偷懒找借口），太久太久没更新文章了，正好趁着今天加班（摸鱼）来写一写最近在项目中封装的自以为很装的组件。在ui疯狂出图的前提条件下，我发现了很多轻提示和弹框dialog高度相似又要支持自定义，便开始了封装之路。</p>
<h2 data-id="heading-1">好孩子要学会先借鉴别人的作业</h2>
<p>我在封装的第一版轻提示中，还是用的老传统props去接收一个visiable控制提示的显示和隐藏，归根结底还是不让组件一上来就挂载在dom节点上。组件写完了自然要使用不是吗，便高高兴兴的提交了代码。我自己在使用的过程中就感觉到很麻烦了，因为还要先引入组件，再定义一个visiable，再在template上写上一个<Toast :xxx="xxx" xxxxxxx/>，再一个页面上如果出现多次调用的话，要么你就多写几个toast（不会吧，不会吧，应该没人会选择这么做吧），要么就疯狂的改变data中定义的数据。虽然自己已经发现了这个弊端，但是不偷懒的程序员不是一个好的程序员，还是选择忽视了这个问题，害，躲的了初一躲不了十五，第二天旁边的仙女同事（她自认为的嘻嘻嘻）就在不经意间吐槽了使用起来过于复杂，完全没有element的好用。内心os：我要是能写的和element差不多就不坐在这了。当然，有其他人也提出了和我相同的问题，那自然要去解决不是吗。</p>
<p>熟练的打开element ui翻到MessageBox组件哪里（此时的我还没意识到自己的项目是vue3环境），发现他们的调用方法也太简单了吧：</p>
<pre><code class="hljs language-vue copyable" lang="vue">
<template>

<el-button type="text" @click="open">点击打开 Message Box</el-button>

</template>

<script>
export default &#123;
  methods: &#123;
    open() &#123;
      this.$alert('这是一段内容', '标题名称', &#123;
        confirmButtonText: '确定',
        callback: action => &#123;
          this.$message(&#123;
            type: 'info',
            message: `action: $&#123; action &#125;`
          &#125;);
        &#125;
      &#125;);
    &#125;
  &#125;
&#125;
</script>

<style>

</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看看自己的代码，简直不能看哈哈哈。古人云：师夷长技以制夷。打开自己开的vue2项目，打开庞大的node_modules包，找到对应的代码开始借鉴。</p>
<h3 data-id="heading-2">第一步，先写好要展示的页面。</h3>
<p>工欲善其事，必先利其器。我们要想组件能使用，自然少不了我们的页面，我们写个demo演示一下：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>测试&#123;&#123;booo&#125;&#125;</div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      visiable: false
    &#125;;
  &#125;
&#125;;
</script>

<style></style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可能有小伙伴会问我写的visiable是干啥的，前面不是才说这个东西会抛弃掉吗？嘿嘿嘿，这里写只是单纯的为了后面测试用的，没有实际作用哈。</p>
<h3 data-id="heading-3">第二步，使用vue构造器创造“子类”</h3>
<p>在翻阅官方文档过程中，我们可以得知vue.extend(options)中的options必须是一个组件，也就是我们前面写的demo，有一点必须要知道的是data必须是一个函数，不过，我相信小伙伴们肯定一直写的都是函数。又因为我们extend创建的不是平常我们写的组件实例，所以不能使用new Vue(&#123; components: test &#125;)，这里官方为我们提供了挂在到节点的方法$mount。千说万说不如直接上代码靠谱。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> Main <span class="hljs-keyword">from</span> <span class="hljs-string">"./main.vue"</span>;
<span class="hljs-keyword">const</span> MessageConstructor = Vue.extend(Main);
<span class="hljs-keyword">let</span> instance;
<span class="hljs-keyword">const</span> Message = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (Vue.prototype.$isServer) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-built_in">console</span>.log(Vue.prototype.$isServer);
  options = options || &#123;&#125;;
  instance = <span class="hljs-keyword">new</span> MessageConstructor(&#123;
    <span class="hljs-attr">data</span>: options
  &#125;);
  instance.$mount();
  <span class="hljs-built_in">document</span>.body.appendChild(instance.$el);
  <span class="hljs-built_in">console</span>.log(instance.visiable);
  <span class="hljs-built_in">console</span>.log(instance.booo);
  <span class="hljs-keyword">return</span> instance;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Message;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在看完代码中，可能会有部分小伙伴会问Vue.prototype.$isServer是什么，说实话，在没看文档前我也不会哈哈哈。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5be5173c1884643bab407118ecbd2f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过文档中可以知道这是判断是否运行在服务器上，我们在服务器上又没有界面自然不需要了。当我们调用方法的时候可以将参数正常传递进来就需要在new构造器的时候接受参数，然后再挂载在$mount上，最后插入到我们的body上.</p>
<h3 data-id="heading-4">第三步，收获成果调用方法</h3>
<p>我们前面的准备工作都做完之后先别着急，怎么会这么容易就让我们可以使用了呢。我们还需要在最外面的main.js导入我们写好的文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> ElementUI <span class="hljs-keyword">from</span> <span class="hljs-string">"element-ui"</span>;
<span class="hljs-keyword">import</span> Message <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/test/main"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"element-ui/lib/theme-chalk/index.css"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;
Vue.use(ElementUI);
<span class="hljs-comment">// Vue.use(Message);</span>
Vue.prototype.$Message = Message;
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以正常使用啦。</p>
<pre><code class="hljs language-vue copyable" lang="vue"> mounted() &#123;
    setTimeout(() => &#123;
      this.$Message(&#123;
        booo: true
      &#125;);
    &#125;, 3000);
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e1e758026ab49d5a669b93435359cc0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这里有人会问这个booo哪里来的，为什么在组件中没有props去接收参数也可以显示，这个就是构造器特殊的地方哈。</p>
<h2 data-id="heading-5">开始在正式项目中使用</h2>
<p>有了前面的铺垫，我自然兴致冲冲的把自己的思路在项目中实践，突然想到自己之前挖的坑项目使用的是vue3,不确定之前写的还可不可以，先放上去试试。果然不出意外的报错了。翻看vue3文档，因为现在不能直接import Vue from "vue";了，所以对应的vue.extend()也没有了。虽然官方删除了extend但是也提供了新的createApp给我们使用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaf7f4e8316d4bb8a3acb4a4cd8c6952~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后改造完的代码如下：</p>
<pre><code class="hljs language-vue copyable" lang="vue">import &#123; createApp &#125; from "vue";
import ToastMessage from "./index.vue";

const createMount = options => &#123;
  const mountNode = document.createElement("div");
  document.body.appendChild(mountNode);

  const app = createApp(ToastMessage, &#123;
    ...options,
    remove() &#123;
      app.unmount(mountNode);
      document.body.removeChild(mountNode);
    &#125;
  &#125;);
  return app.mount(mountNode);
&#125;;

const toast = options => &#123;
  return createMount(options);
&#125;;

toast.install = app => &#123;
  app.component("Toast", ToastMessage);
  app.config.globalProperties.$toast = toast;
&#125;;

export default toast;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里小伙伴们要注意了，在vue2中我们可以不用props接受数据也可以显示出来，但是vue3不行了哦。</p>
<h2 data-id="heading-6">后记</h2>
<p>希望这篇文章能对大家有所帮助，如果有写的不对的地方也希望指点一二。</p>
<pre><code class="copyable">                                                            --wy白菜
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            