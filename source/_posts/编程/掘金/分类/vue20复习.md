
---
title: 'vue2.0复习'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Sun, 02 May 2021 04:13:01 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue</h1>
<h1 data-id="heading-1">用vue-cli创建一个vue项目</h1>
<ol>
<li>安装</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g @vue/cli
<span class="hljs-comment"># OR</span>
yarn global add @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建项目</p>
<pre><code class="hljs language-bash copyable" lang="bash">vue create my-project
<span class="hljs-comment"># OR</span>
vue ui
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>安装配置：具体配置按具体情况来</p>
<p>第一步</p>
<p>? Please pick a preset: (Use arrow keys)</p>
<blockquote>
<p>Default ([Vue 2] babel, eslint)  //默认vue2配置
Default (Vue 3 Preview) ([Vue 3] babel, eslint) //默认vue3配置
Manually select features            //手动配置</p>
</blockquote>
</li>
</ol>
<p>第二步</p>
<p>​    ? Check the features needed for your project: (Press  to select, <a href="https://juejin.cn/post/undefined"> to toggle all, <i> to invert      selection)</i></a></p><a href="https://juejin.cn/post/undefined"><i>
<blockquote>
<p>(<em>) Choose Vue version                             //选择vue版本
(</em>) Babel                                                   //转码器，将es6变为es5
( ) TypeScript                                          //TypeScript是一个JavaScript（后缀.js）的超集（后缀.ts）
( ) Progressive Web App (PWA) Support     // 渐进式Web应用程序
( ) Router                                               //路由
( ) Vuex //状态管理
( ) CSS Pre-processors//CSS预处理器如less，sass
() Linter / Formatter                        // 代码规范和报错
( ) Unit Testing //单元测试
( ) E2E Testing                                      //end to end测试</p>
</blockquote>
<p>第三步
? Choose a version of Vue.js that you want to start the project with (Use arrow keys)</p>
<blockquote>
<p>2.x                                //vue2.0
3.x (Preview)              //vue3.0</p>
</blockquote>
<p>第四步
? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n)    //使用什么路由模式，  我经常选n，使用hash模式</p>
<p>第五步
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): (Use arrow keys)                   //使用那种css的预处理器</p>
<blockquote>
<p>Sass/SCSS (with dart-sass)
Sass/SCSS (with node-sass)
Less//我经常用
Stylus</p>
</blockquote>
<p>第六步
? Pick a linter / formatter config: (Use arrow keys)        //选择那种代码规则</p>
<blockquote>
<p>ESLint with error prevention only
ESLint + Airbnb config
ESLint + Standard config
ESLint + Prettier                                               //我经常用</p>
</blockquote>
</i></a><i><p><a href="https://juejin.cn/post/undefined">第七步
? Pick additional lint features: (Press  to select, </a><a href="https://juejin.cn/post/undefined"> to toggle all, <i> to invert selection)</i></a></p><a href="https://juejin.cn/post/undefined"><i>
<blockquote>
<p>(*) Lint on save//保存就检测
( ) Lint and fix on commit                      //fix和commit时检测</p>
</blockquote>
<p>第八步
? Pick a unit testing solution: (Use arrow keys)</p>
<blockquote>
<p>Mocha + Chai  //mocha灵活,只提供简单的测试结构，如果需要其他功能需要添加其他库/插件完成。必须在全局环境中安装
Jest    //安装配置简单，容易上手。内置Istanbul，可以查看到测试覆盖率，相较于Mocha:配置简洁、测试代码简洁、易于和babel集成、内置丰富的expect</p>
</blockquote>
<p>第九步
? Where do you prefer placing config for Babel, ESLint, etc.?
In dedicated config files     //独立文件放置</p>
<blockquote>
<p>In package.json                  //存放在package.json中</p>
</blockquote>
<p>第十步
? Save this as a preset for future projects? (y/N) //是否保存配置</p>
<p>vue项目创建完毕。</p>
<p>我们打开我们创建的文件，先打开src里面的app.vue。</p>
<p><img alt="1616896148882" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>里面全部删除，敲上如下代码</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">

  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;

      &#125;
    &#125;,
    methods: &#123;
    
  &#125;
&#125;
</script>

<style lang="less">
#app &#123;

&#125;

</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>template内是html，需要且只有有一个根元素</p>
<p>script内data写数据，methods写逻辑</p>
<p>style内写样式</p>
<h1 data-id="heading-2">数据绑定</h1>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    &#123;&#123;a&#125;&#125;
    <!-- 插值表达式，可以将data里面的值显示到页面 -->
    &#123;&#123;a+2&#125;&#125;
    <!-- 可以输出简单的表达式的结果 -->
    &#123;&#123;a+3>2? '大':'小'&#125;&#125;
    <!-- 可以用三元表达式 -->
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        a:'1'
      &#125;
    &#125;,
    methods: &#123;
    
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>双向数据绑定</strong>：data的值变化时，页面的数据也会跟着变化，页面的数据变化，data的值也会发生变化</p>
<p><strong>nextTick()</strong>:获取dom更新后的数据</p>
<h1 data-id="heading-3">指令</h1>
<p>指令是带有v-开头的特殊指令</p>
<h2 data-id="heading-4">v-block</h2>
<h2 data-id="heading-5">v-text</h2>
<p>和插值表达式差不多，显示data的数据</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1 v-text="msg"></h1>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: 'Hello Vue.'
      &#125;
    &#125;,
    methods: &#123;
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">v-html</h2>
<p>和v-text差不多，这里可以解析html标签</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <div v-html="msg"></div>
    
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: '<h1>Hello Vue.</h1>'
      &#125;
    &#125;,
    methods: &#123;
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">v-pre</h2>
<p>其和其子元素跳过编译，直接显示，加快性能，</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <div v-pre>&#123;&#123;msg&#125;&#125;</div>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: '<h1>Hello Vue.</h1>'
      &#125;
    &#125;,
    methods: &#123;
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">v-once</h2>
<p>只渲染一次，后面再也不改动</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <p @click="add">点击变化：&#123;&#123; a &#125;&#125;</p>
    <p v-once @click="add">点击不变：&#123;&#123; a &#125;&#125;</p>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: '<h1>Hello Vue.</h1>',
        a:1
      &#125;
    &#125;,
    methods: &#123;
      add()&#123;
        this.a++
      &#125;
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">v-show</h2>
<p>显示和隐藏，设置元素属性display：none；</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1 v-show="true">&#123;&#123;msg&#125;&#125;显示</h1>
    <h1 v-show="false">&#123;&#123;msg&#125;&#125;</h1>不显示
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: 'Hello Vue.',
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">v-if,v-else-if,v-else</h2>
<p>如同if...else if....else....的用法，这里隐藏后元素都不会出现</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <p v-if="nub>3">大于</p>
    <p v-else-if="nub=3">等于</p>
    <p v-else>小于</p>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        nub: 3,
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">v-for</h2>
<p>可以自动帮你循环数组和对象</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <ul>
      <li v-for="(val,key) in No" :key="key">
<!-- val是值，key是属性名，key是用于虚拟dom查找用的，不写没用语法错误，但正常都要写上，不如可能会出问题 -->
        &#123;&#123;key+"---"+val&#125;&#125;
      </li>
    </ul>
    <ul>
      <li v-for="(value,index) in No.girlfriend" :key="index">
<!-- value是值，index是索引 -->
        &#123;&#123; value&#125;&#125;
      </li>
    </ul>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        No:&#123;
          name:"不忘",
          age:"20",
          girlfriend:['冰冰','黑嘉嘉','雷姆']
        &#125;
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">v-model</h2>
<p>表单的数据绑定</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
   <input type="text" v-model="msg">
   <br>
   表单的内容：&#123;&#123;msg&#125;&#125;
  <!-- 表单的值改变msg的值，msg改变，页面的值也跟着改变，这就可以看到什么是双向数据绑定 -->

  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: "",
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">有关v-model的修饰符</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
   <input type="text" v-model.lazy="msg">
   <br>
   表单的内容：&#123;&#123;msg&#125;&#125;
  <!-- 此时失去焦点值才会发生变化 -->

  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;
        msg: "",
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用的修饰符</p>
<p>改成change方法：lazy</p>
<p>输入数字：number</p>
<p>去除首尾空白：trim</p>
<h2 data-id="heading-14">v-bind</h2>
<p>属性绑定，有时候属性是动态的，绑定后就可以改变值简写是：</p>
<h3 data-id="heading-15">基础用法</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <a :href="url">去</a>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        url: "http://www.baidu.com/",
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
#app &#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">绑定class（对象）</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app"> 
  <h1 :class="&#123;red:isred&#125;">hello world. </h1>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        isred:true,
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
 .red&#123;
    color: red;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">绑定class（数组）</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <h1 :class="['red']">hello world. </h1>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>
 .red&#123;
    color: red;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">绑定style</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <h1 :style="&#123;color:col&#125;">hello world. </h1>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        col:'red'
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">绑定style(数组)</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  
  <h1 :style="[col]">hello world. </h1>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        col:&#123;color:'red'&#125;
      &#125;
    &#125;,
    methods: &#123;
     
  &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">v-on</h2>
<p>绑定事件，简写@</p>
<h3 data-id="heading-21">基础用法</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <p>&#123;&#123;a&#125;&#125;</p>
  <button @click="add">加一</button>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        a:1
      &#125;
    &#125;,
    methods: &#123;
     add()&#123;
       this.a++
     &#125;
  &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用的事件有：</p>
<p>单击：click</p>
<p>双击：dblclick</p>
<p>鼠标移入：mouseover</p>
<p>鼠标移出：mouseleave</p>
<p>鼠标移动：mousemove</p>
<p>获取焦点：focus</p>
<p>失去焦点：blue</p>
<p>按键弹起：keyup</p>
<p>按键按下：keydown</p>
<h3 data-id="heading-22">传递参数</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <p>&#123;&#123;a&#125;&#125;</p>
  <button @click="add(2)">加二</button>
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        a:1
      &#125;
    &#125;,
    methods: &#123;
     add(nub)&#123;
       this.a=this.a+nub;
     &#125;
  &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">有关v-on的修饰符</h3>
<p>可以对事件进行一定规定</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <a href="https://www.baidu.com/" @click.prevent="add">加一去</a>
      <!-- a链接不发生跳转因为阻止默认事件了 -->
  &#123;&#123;a&#125;&#125;
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        a:1
      &#125;
    &#125;,
    methods: &#123;
     add()&#123;
       this.a++
     &#125;
  &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用的修饰符有</p>
<p>停止冒泡：stop</p>
<p>阻止默认行为：prevent</p>
<p>只触发一次：once</p>
<p>自触发自身：self</p>
<p>键盘触发的按键：.enter    或者.按键码</p>
<p>修饰符可以连用，且有先后顺序问题</p>
<h2 data-id="heading-24">自定义指令</h2>
<h1 data-id="heading-25">过滤器filter</h1>
<p>可以将数据按照固定格式修改</p>
<h2 data-id="heading-26">全局过滤器</h2>
<p>所有文件都可以使用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <p>&#123;&#123;name | no&#125;&#125;</p>
  </div>
</template>
<script>

export default &#123;
    data()&#123;
      return &#123;
        name:"不忘"
      &#125;
    &#125;,
    methods: &#123;
     
    &#125;,

&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是使用过滤器，全局过滤器需要在main.js定义</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> ElementUI <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/index.css'</span>;

Vue.use(ElementUI);

Vue.filter(<span class="hljs-string">'no'</span>,<span class="hljs-function"><span class="hljs-params">_</span>=></span>&#123;<span class="hljs-comment">//全局过滤器</span>
  <span class="hljs-keyword">return</span> _+<span class="hljs-string">'最帅'</span>
&#125;)

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
&#125;).$mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">局部过滤器</h2>
<p>当前文件可以使用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <p>&#123;&#123;name | no&#125;&#125;</p>
  </div>
</template>
<script>

export default &#123;
    data()&#123;
      return &#123;
        name:"不忘"
      &#125;
    &#125;,
    methods: &#123;
     
    &#125;,
  filters:&#123;
    no(msg)&#123;
      return msg+'最帅'
    &#125;
  &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-28">侦听器watch</h1>
<p>可以监听数据变化，当数据变化时触发</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
  <p>&#123;&#123;a&#125;&#125;</p>
  <button @click="add">加一</button>
  <br>
  现在的值：&#123;&#123;newval&#125;&#125;
  <br>
  之前的值：&#123;&#123;old&#125;&#125;
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        a:1,
        newval:'',
        old:''
      &#125;
    &#125;,
    methods: &#123;
     add()&#123;
       this.a++
     &#125;
    &#125;,
    watch:&#123;
      a(newval,old)&#123;
        //第一个参数是改变后的值，第二个是改变前的值
        this.newval=newval
        this.old=old
      &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-29">计算属性computed</h1>
<p>在&#123;&#123;&#125;&#125;放入太多逻辑会加大计算机处理，在computed内会将数据修改后保存</p>
<p><strong>computed内是属性名不能和data中一样</strong></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    &#123;&#123;fullname&#125;&#125;
  </div>
</template>
<script>
export default &#123;
    data()&#123;
      return &#123;
        firstname:'东方',
        lastname:'老赢',
      &#125;
    &#125;,
    methods: &#123;
     
    &#125;,
    computed:&#123;
      fullname()&#123;
        return this.firstname + '-' + this.lastname;
      &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-30">组件</h1>
<p>组件就是自己定义一段html，然后用一个标签就可以引用，经常用的html片段就可以封装成一个组件</p>
<h2 data-id="heading-31">全局注册</h2>
<p>在component的文件夹下创建son.vue文件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <h1>为天地立心</h1>
  </div>
</template>
<script>
export default &#123;
    name:'son',
    data()&#123;
      return &#123;
        message:'hellow vue.',
        isShow:true,
      &#125;
    &#125;,
    methods: &#123;
    
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.js文件下创建</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> ElementUI <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/index.css'</span>;

Vue.use(ElementUI);

<span class="hljs-keyword">import</span> son <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/son.vue'</span>; <span class="hljs-comment">//导入son.vue</span>
Vue.component(<span class="hljs-string">'Son'</span>, son)<span class="hljs-comment">//设置全局组件</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
&#125;).$mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在app.vue中使用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <Son />
    <!-- 使用组件 -->
  </div>
</template>
<script>
export default &#123;
    name:'app',
    data()&#123;
      return &#123;
      &#125;
    &#125;,
    methods: &#123;
    
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">局部注册</h2>
<p>和上面一样在component的文件夹下创建son.vue文件</p>
<p>然后再app.vue上使用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <Son />
    <!-- 使用组件 -->
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
    name:'app',
    components: &#123;
      Son
    &#125;,
    data()&#123;
      return &#123;
      &#125;
    &#125;,
    methods: &#123;
     
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">组件传值</h2>
<h3 data-id="heading-34">父传子</h3>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <Son :fatherMsg="msg"/>
    <!-- 将要传的值属性绑定在标签上 -->
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
    name:'app',
    components: &#123;
      Son
    &#125;,
    data()&#123;
      return &#123;
        msg:'为生民立命'
      &#125;
    &#125;,
    methods: &#123;
   
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <h1>为天地立心</h1>
    <h1>&#123;&#123;fatherMsg&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
    name:'son',
    //使用props接受父组件的值，有两种写法
    props:['fatherMsg'],
    // props:&#123;
    //     fatherMsg: &#123;
    //         required: true,//必填
    //         type: String,//字符串类型
    //     &#125;
    // &#125;,
    data()&#123;
      return &#123;
    
      &#125;
    &#125;,
    methods: &#123;
  
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">子传父</h3>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <Son @sonShow="fatherShow"/>
      <!-- 用方法绑定传递fatherShow方法 -->
    <h1>&#123;&#123;msg&#125;&#125;</h1>
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
    name:'app',
    components: &#123;
      Son
    &#125;,
    data()&#123;
      return &#123;
        msg:''
      &#125;
    &#125;,
    methods: &#123;
     fatherShow(sonMsg)&#123;
       this.msg=sonMsg
     &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <button @click="show">出现</button>
    <h1>为天地立心</h1>
  </div>
</template>
<script>
export default &#123;
    name:'son',
    data()&#123;
      return &#123;
        msg:'为生民立命',
      &#125;
    &#125;,
    methods: &#123;
     show()&#123;
       this.$emit('sonShow',this.msg)//用sonShow接收方法，并将给父组件的数据加到参数内
     &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">Even bus传值</h3>
<p>在src下创建utils文件夹，在创建bus.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> eventbus = <span class="hljs-keyword">new</span> Vue()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    &#123;&#123;didi&#125;&#125;
    <button @click="givege">获取弟弟的消息</button>
  </div>
</template>
<script>
import &#123;eventbus&#125; from '../utils/bus.js'
export default &#123;
    name:'son',
    data()&#123;
      return &#123;
        didi:'',
        a:'今朝有酒今朝醉'
      &#125;
    &#125;,
    methods: &#123;
      givege()&#123;
        eventbus.$emit('givege',this.a)
      &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建兄弟组件borther.vue</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    &#123;&#123;gege&#125;&#125;
    <button @click='givedi'>获取哥哥的消息</button>
  </div>
</template>
<script>
import &#123;eventbus&#125; from '../utils/bus.js'
export default &#123;
    name:'app',
    data()&#123;
      return &#123;
       gege:'',
       b:'明日愁来明日愁'
      &#125;
    &#125;,
    methods: &#123;
      givedi()&#123;
        eventbus.$emit('givedi',this.b)
      &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在app.vue</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <Son />
    <Borther />
  </div>
</template>
<script>
import Son from "./components/son"
import Borther from "./components/brother"
import &#123;eventbus&#125; from './utils/bus.js'
export default &#123;
    name:'app',
    components:&#123;
      Son,Borther
    &#125;,
    data()&#123;
      return &#123;
     
      &#125;
    &#125;,
    methods: &#123;
    &#125;,
    mounted()&#123;
      eventbus.$on('givedi',data=>&#123;
        console.log(data);
      &#125;)
      eventbus.$on('givege',data=>&#123;
        console.log(data);
      &#125;)
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">多级组件传值</h3>
<h4 data-id="heading-38"><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">attrs/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord">/</span></span></span></span></span>listeners</h4>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
      <h1>为天地立心</h1>
    <Son :msg="msg" :msgT="msgT" :msgS="msgS" @father="father" @gfather="gfather"/>
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
    name:'app',
    components: &#123;
      Son
    &#125;,
    data()&#123;
      return &#123;
        msg:'为生民立命',
        msgT:'继往圣绝学',
        msgS:'为万世开太平'
      &#125;
    &#125;,
    methods: &#123;
      father()&#123;
        console.log("666");
      &#125;,
      gfather() &#123;
        console.log("牛比");
      &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <h1>&#123;&#123;msg&#125;&#125;</h1>
    <h1>&#123;&#123;$attrs&#125;&#125;</h1>
    <Gson v-bind="$attrs" v-on="$listeners"/>
  </div>
</template>
<script>
import Gson from "./gson";
export default &#123;
    name:'son',
    inheritAttrs:false,// 可以关闭自动挂载到组件根元素上的没有在props声明的属性
    props:['msg'],//这里截取后孙子就获取不到了
    components:&#123;
        Gson
    &#125;,
    data()&#123;
      return &#123;
    
      &#125;
    &#125;,
    methods: &#123;
      
    &#125;,
    mounted()&#123;
      this.$emit('father')
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件的子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <h1>&#123;&#123;msgT&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
    name:'son',
    inheritAttrs:false,
    props:['msgT'],
    data()&#123;
      return &#123;
    
      &#125;
    &#125;,
    methods: &#123;
  
    &#125;,
    mounted()&#123;
      this.$emit('gfather')
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">provide/inject</h4>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1>为天地立心</h1>
    <Son/>
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
    name:'app',
    components: &#123;
      Son
    &#125;,
    data()&#123;
      return &#123;
      &#125;
    &#125;,
    provide: &#123;
      msgT:'为生民立命',
      msgS:'为继往圣绝学'
    &#125;,
    methods: &#123;
     
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <h1>&#123;&#123;msgT&#125;&#125;</h1>
    <Gson />
  </div>
</template>
<script>
import Gson from "./gson";
export default &#123;
    name:'son',
    inject:['msgT'],
    components:&#123;
        Gson
    &#125;,
    data()&#123;
      return &#123;
    
      &#125;
    &#125;,
    methods: &#123;
      
    &#125;,
    mounted()&#123;
      this.$emit('father')
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件的子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <h1>&#123;&#123;msgS&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
    name:'son',
    inject:['msgS'],
    data()&#123;
      return &#123;
    
      &#125;
    &#125;,
    methods: &#123;
  
    &#125;,
    mounted()&#123;
      this.$emit('gfather')
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">vuex</h2>
<p>看下面</p>
<h1 data-id="heading-41">插槽</h1>
<p>在父组件添加子组件的内容</p>
<h3 data-id="heading-42">普通插槽</h3>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1>为天地立心</h1>
    <Son>
      <h1>为万世开太平</h1>
     <!-- 写到子组件的内容 -->
    </Son>
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
  name: 'app',
  components: &#123;
    Son
  &#125;,
  data () &#123;
    return &#123;
    &#125;
  &#125;,
  methods: &#123;
  &#125;
&#125;
</script>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
      <h1>为生民立命</h1>
      <slot></slot>
   <!-- 父组件内容存放的位置-->
  </div>
</template>
<script>
export default &#123;
  name: 'app',
  data () &#123;
    return &#123;
    &#125;
  &#125;,
  methods: &#123;
  &#125;
&#125;
</script>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">具名插槽</h3>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <Son>
      <template v-slot:header>
        <h1>为天地立心</h1>
      </template>
      <template v-slot:footer>
        <h1>为万世开太平</h1>
      </template>
    </Son>
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
  name: 'app',
  components: &#123;
    Son
  &#125;,
  data () &#123;
    return &#123;
    &#125;
  &#125;,
  methods: &#123;
  &#125;
&#125;
</script>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
      <slot name="header"></slot>
      <h1>为生民立命</h1>
      <slot name="footer"></slot>
  </div>
</template>
<script>
export default &#123;
  name: 'app',
  data () &#123;
    return &#123;
    &#125;
  &#125;,
  methods: &#123;
  &#125;
&#125;
</script>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">作用域插槽</h3>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1>为天地立心</h1>
    <Son>
     <template v-slot:default="soldata">
       <h1>&#123;&#123;soldata.data&#125;&#125;</h1>
     </template>
    </Son>

    <!-- <Son  v-slot:default="soldata">
       <h1>&#123;&#123;soldata.data&#125;&#125;</h1>
    </Son> -->

    <!-- <Son  v-slot="soldata">
       <h1>&#123;&#123;soldata.data&#125;&#125;</h1>
    </Son> -->
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
  name: 'app',
  components: &#123;
    Son
  &#125;,
  data () &#123;
    return &#123;
    &#125;
  &#125;,
  methods: &#123;
  &#125;
&#125;
</script>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
      <h1>为生民立命</h1>
      <slot :data="msg">&#123;&#123;msg&#125;&#125;</slot>
  </div>
</template>
<script>
export default &#123;
  name: 'app',
  data () &#123;
    return &#123;
      msg: '为万世开太平'
    &#125;
  &#125;,
  methods: &#123;
  &#125;
&#125;
</script>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-45">vue生命周期钩子函数</h1>
<p>一个组件从开始到消亡所经历的全部过程，就是一个组件的生命周期</p>
<p>简单讲就是你看到组件在页面出现和消失的过程，在这个过程中会自动触发几个函数，就是生命周期钩子函数</p>
<p>父组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1 @click="change">让组件消失</h1>
    <Son v-if="isShow"/>
  </div>
</template>
<script>
import Son from './components/son'
export default &#123;
    name:'app',
    components: &#123;
      Son
    &#125;,
    data()&#123;
      return &#123;
        isShow:true
      &#125;
    &#125;,
    provide: &#123;
      msgT:'为生民立命',
      msgS:'为继往圣绝学'
    &#125;,
    methods: &#123;
     change()&#123;
       this.isShow=false;
     &#125;
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="son">
    <button @click="change">&#123;&#123;!isShow?'出现':"消失"&#125;&#125;</button>
    <h1 v-if="isShow">&#123;&#123;message&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
    name:'son',
    data()&#123;
      return &#123;
        message:'hellow vue.',
        isShow:false,
      &#125;
    &#125;,
    methods: &#123;
     change()&#123;
       this.isShow = !this.isShow;
     &#125;
    &#125;,
     beforeCreate()&#123;
      console.group('------beforeCreate创建前状态------');
      console.log("%c%s", "color:red" , "el     : " + this.$el); //undefined
      console.log("%c%s", "color:red","data   : " + this.$data); //undefined 
      console.log("%c%s", "color:red","message: " + this.message) //undefined 
    &#125;,
    created()&#123;
      console.group('------created创建完毕状态------');
      console.log("%c%s", "color:red","el     : " + this.$el); //undefined
      console.log("%c%s", "color:red","data   : " + this.$data); //已被初始化 
      console.log("%c%s", "color:red","message: " + this.message); //已被初始化
    &#125;,
    beforeMount()&#123;
      console.group('------beforeMount挂载前状态------');
      console.log("%c%s", "color:red","el     : " + (this.$el)); //undefined
      //此时应该是已经初始化但数据未加载上去，但结果确实未underfind，不是很了解情况，各位可以自己尝试一下
      console.log("%c%s", "color:red","data   : " + this.$data); //已被初始化  
      console.log("%c%s", "color:red","message: " + this.message); //已被初始化  
    &#125;,
    mounted()&#123;
      console.group('------mounted 挂载结束状态------');
      console.log("%c%s", "color:red","el     : " + this.$el); //已被初始化
      console.log(this.$el);    
      console.log("%c%s", "color:red","data   : " + this.$data); //已被初始化
      console.log("%c%s", "color:red","message: " + this.message); //已被初始化 
    &#125;,
    beforeUpdate()&#123;
      console.group('beforeUpdate 更新前状态===============》');
      console.log("%c%s", "color:red","el     : " + this.$el);
      console.log(this.$el);   
      console.log("%c%s", "color:red","data   : " + this.$data); 
      console.log("%c%s", "color:red","message: " + this.message); 
    &#125;,
    updated()&#123;
      console.group('updated 更新完成状态===============》');
      console.log("%c%s", "color:red","el     : " + this.$el);
      console.log(this.$el); 
      console.log("%c%s", "color:red","data   : " + this.$data); 
      console.log("%c%s", "color:red","message: " + this.message); 
    &#125;,
    beforeDestroy()&#123;
      console.group('beforeDestroy 销毁前状态===============》');
      console.log("%c%s", "color:red","el     : " + this.$el);
      console.log(this.$el);    
      console.log("%c%s", "color:red","data   : " + this.$data); 
      console.log("%c%s", "color:red","message: " + this.message); 
    &#125;,
    destroyed()&#123;
      console.group('destroyed 销毁完成状态===============》');
      console.log("%c%s", "color:red","el     : " + this.$el);
      console.log(this.$el);  
      console.log("%c%s", "color:red","data   : " + this.$data); 
      console.log("%c%s", "color:red","message: " + this.message)
    &#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-46">vue路由</h1>
<p>单页面应用（SPA），第一次加载页面，后面全部都是获取数据，加快页面的响应速度，不利于seo</p>
<p>这里页面跳转变成了路由跳转</p>
<p>由于我用的是脚手架，所以vue-router已经配置好了，可以打开router文件下的index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
   <span class="hljs-comment">//这里配置路由</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,<span class="hljs-comment">//路径</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,<span class="hljs-comment">//路由名</span>
    <span class="hljs-attr">component</span>: Home<span class="hljs-comment">//指向的组件</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
    <span class="hljs-comment">// route level code-splitting</span>
    <span class="hljs-comment">// this generates a separate chunk (about.[hash].js) for this route</span>
    <span class="hljs-comment">// which is lazy-loaded when the route is visited.</span>
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "about" */</span> <span class="hljs-string">'../views/About.vue'</span>)
  &#125;
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router

<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改app.vue</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <router-view />
    <!-- 路由开启,开始按照路由的文件导入组件 -->
  </div>
</template>

<style>
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">路由跳转</h2>
<h3 data-id="heading-48">router-link</h3>
<p>不带参数</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
<router-link :to="&#123;name:'home'&#125;">跳转</router-link>
<router-link :to="&#123;path:'/home'&#125;">跳转</router-link>
<!-- 注意：router-link中链接如果是'/'开始就是从根路由开始，如果开始不带'/'，则从当前路由开始。 -->
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>带参数</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
<router-link :to="&#123;name:'home', params: &#123;id:1&#125;&#125;"> 跳转</router-link>
     <!-- 
        在url路径中看不到
        html 取参  $route.params.id
        script 取参  this.$route.params.id
    -->
<router-link :to="&#123;name:'home', query: &#123;id:1&#125;&#125;"> 跳转</router-link>
      <!-- 
        在url路径中可以看到
        html 取参  $route.query.id
        script 取参  this.$route.query.id
    -->
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-49">this.$router.push()</h3>
<p>不带参数</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
<button @click="add">跳转</button>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;

      &#125;
    &#125;,
    methods: &#123;
    go()&#123;
            this.$router.push('/home') 
            //this.$router.push(&#123;name:'home'&#125;) 
            //this.$router.push(&#123;path:'/home'&#125;)
        &#125;
  &#125;
&#125;
</script>

<style lang="less">
#app &#123;

&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>带参数</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
<button @click="add">跳转</button>
  </div>
</template>

<script>
export default &#123;
    data()&#123;
      return &#123;

      &#125;
    &#125;,
    methods: &#123;
    go()&#123;
            this.$router.push(&#123;name:'home',query: &#123;id:'1'&#125;&#125;)
   //this.$router.push(&#123;path:'/home',query: &#123;id:'1'&#125;&#125;)
            //html 取参  $route.query.id
            //script 取参  this.$route.query.id
           
            //this.$router.push(&#123;name:'home',params: &#123;id:'1'&#125;&#125;) 
            // html 取参  $route.params.id
   // script 取参  this.$route.params.id
        &#125;
  &#125;
&#125;
</script>

<style lang="less">
#app &#123;

&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-50">this.$router.replace() t</h3>
<p>用法和this.$router.push() 一样，就是history不会有记录，返回不了</p>
<h3 data-id="heading-51">this.$router.go(n)</h3>
<p>整数向前，负数向后跳转n次，多用来做返回</p>
<h1 data-id="heading-52">导航守卫</h1>
<p>有些页面可以跳转有些页面不能跳转，这时候就需要导航守卫了</p>
<h2 data-id="heading-53">全局</h2>
<p>写在router的index.js中</p>
<p>router.beforeEach（全局前置守卫） ：所以路由跳转前都会执行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
    <span class="hljs-comment">//to : 将要进入的目标路由对象</span>
    <span class="hljs-comment">//from : 即将离开的目标路由对象</span>
    <span class="hljs-comment">//next:执行跳转的下一步钩子,执行才会进入下一步，否则不会跳转</span>
    next()
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>router.beforeResolve() (全局解析守卫) ，和router.beforeEach差不多</p>
<p>router.afterEach() (全局后置钩子) ：和router.beforeEach差不多，区别路由已经跳转，所以没有next</p>
<h2 data-id="heading-54">独享</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
   <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
   <span class="hljs-attr">name</span>: <span class="hljs-string">'about'</span>,
   <span class="hljs-attr">component</span>: about,
   <span class="hljs-attr">beforeEnter</span>:<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>)=></span>&#123;
      <span class="hljs-built_in">console</span>.log(to);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">from</span>);
      next()
   &#125;
   <span class="hljs-comment">//和 router.beforeEach差不多，这是单个路由用的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-55">组件内</h2>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>关于页面</div>
</template>
<script>
  export default &#123;
    name: "about",
    beforeRouteEnter(to, from, next) &#123;
      //进入该路由时执行
    &#125;,
    beforeRouteUpdate(to, from, next) &#123;
      //该路由参数更新时执行,同一个路由，参数改变时执行
    &#125;,
    beforeRouteLeave(to, from, next) &#123;
      //离开该路由时执行
    &#125;
  &#125;
</script>
<style scoped>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-56">vuex</h1>
<p>使用脚手架，vuex的基本配置也弄好了，可以看到store文件夹下的index.js，vuex会将需要的数据保存，各个组件都可以调用</p>
<h2 data-id="heading-57">state</h2>
<p>保存数据状态</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">'不忘'</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <h1>&#123;&#123;$store.state.name&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
  methods: &#123;
    test () &#123;
      console.log(this.$store.state.name)
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-58">mutations</h2>
<p>修改state的数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">'不忘'</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params">state</span>)</span>&#123;<span class="hljs-comment">//可以加第二个参数，接受调用传递过来的参数</span>
          state.name=<span class="hljs-string">"回忆"</span>
      &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件调用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <h1>&#123;&#123;$store.state.name&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
  methods: &#123;
    test () &#123;
      this.$store.commit('change')
       //可以在后面加参数
        //this.$store.commit('change',参数)
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-59">增加删除state的数据</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.set(state,<span class="hljs-string">"age"</span>,<span class="hljs-number">15</span>)<span class="hljs-comment">//增加</span>
Vue.delete(state,<span class="hljs-string">'age'</span>)<span class="hljs-comment">//删除</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-60">getters</h3>
<p>对数据加工</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;

Vue.use(Vuex);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'不忘'</span>,
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">fullname</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">const</span> a = <span class="hljs-string">`姓名:<span class="hljs-subst">$&#123;state.name&#125;</span>`</span>;
      <span class="hljs-keyword">return</span> a;
    &#125;,
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <h1>&#123;&#123;$store.getters.fullname&#125;&#125;</h1>
  </div>
</template>
<script>
export default &#123;
  methods: &#123;
    
  &#125;,
&#125;;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-61">aciton</h2>
<p>操作异步方法修改state</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;

Vue.use(Vuex);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'不忘'</span>,
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params">state, data</span>)</span> &#123;
      state.name = data;
    &#125;,
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">useChange</span>(<span class="hljs-params">context, payload</span>)</span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        context.commit(<span class="hljs-string">'change'</span>, payload);
      &#125;, <span class="hljs-number">1000</span>);
    &#125;,
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <h1>&#123;&#123;$store.state.name&#125;&#125;</h1>
    <button @click="change">改变</button>
  </div>
</template>
<script>
export default &#123;
  methods: &#123;
    change() &#123;
      this.$store.dispatch('useChange', '回忆');
    &#125;,
  &#125;,
&#125;;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-62">modules</h2>
<p>对vuex内数据分类，调用和前面差不多</p>
<h1 data-id="heading-63">vue.config.js</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 部署生产环境和开发环境下的URL。</span>
  <span class="hljs-comment">// 默认情况下，Vue CLI 会假设你的应用是被部署在一个域名的根路径上</span>
  <span class="hljs-comment">// 例如 https://www.ruoyi.vip/。如果应用被部署在一个子路径上，你就需要用这个选项指定这个子路径。例如，如果你的应用被部署在 https://www.ruoyi.vip/admin/，则设置 baseUrl 为 /admin/。</span>
  <span class="hljs-attr">publicPath</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-string">"/"</span> : <span class="hljs-string">"/"</span>,
  <span class="hljs-comment">// 在npm run build 或 yarn build 时 ，生成文件的目录名称（要和baseUrl的生产环境路径一致）（默认dist）</span>
  <span class="hljs-attr">outputDir</span>: <span class="hljs-string">'dist'</span>,
  <span class="hljs-comment">// 用于放置生成的静态资源 (js、css、img、fonts) 的；（项目打包之后，静态资源会放在这个文件夹下）</span>
  <span class="hljs-attr">assetsDir</span>: <span class="hljs-string">'static'</span>,
  <span class="hljs-comment">// 是否开启eslint保存检测，有效值：ture | false | 'error'</span>
  <span class="hljs-attr">lintOnSave</span>: process.env.NODE_ENV === <span class="hljs-string">'development'</span>,
  <span class="hljs-comment">// 如果你不需要生产环境的 source map，可以将其设置为 false 以加速生产环境构建。</span>
  <span class="hljs-attr">productionSourceMap</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">// webpack-dev-server 相关配置</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'0.0.0.0'</span>,<span class="hljs-comment">//服务器地址</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,<span class="hljs-comment">//开启端口</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//是否自动代开网页</span>
    <span class="hljs-attr">proxy</span>: &#123;<span class="hljs-comment">//代理服务器，解决跨域问题</span>
      <span class="hljs-comment">// detail: https://cli.vuejs.org/config/#devserver-proxy</span>
      [process.env.VUE_APP_BASE_API]: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">`http://192.168.1.53:8080`</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          [<span class="hljs-string">'^'</span> + process.env.VUE_APP_BASE_API]: <span class="hljs-string">''</span>
        &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">disableHostCheck</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-attr">configureWebpack</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'不忘'</span>,<span class="hljs-comment">//标题</span>
    <span class="hljs-attr">resolve</span>: &#123;
      <span class="hljs-attr">alias</span>: &#123;
        <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'src'</span>)<span class="hljs-comment">//导入文件时路径@/开头表示src/开头</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置比较复杂，各位可以自己尝试</p></i></a></i></div>  
</div>
            