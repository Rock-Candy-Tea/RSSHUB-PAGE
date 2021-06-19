
---
title: 'vue3+vite+typeScript+eslint创建一个vue3项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=645'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 02:28:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=645'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">创建项目</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建项目命令</span>
# npm <span class="hljs-number">6.</span>x
npm init @vitejs/app my-vue-app --template vue

# npm <span class="hljs-number">7</span>+, 需要额外的双横线：
npm init @vitejs/app my-vue-app -- --template vue

# yarn
yarn create @vitejs/app my-vue-app --template vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tips：使用yarn的时候会报错，不知道为什么，有大佬知道的麻烦告知一下</p>
<p>项目创建完成之后</p>
<pre><code class="hljs language-js copyable" lang="js">cd my-project

npm install
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">引入路由</h3>
<pre><code class="hljs language-js copyable" lang="js">npm i vue-router@<span class="hljs-number">4.0</span><span class="hljs-number">.9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建router文件夹，并在文件夹中创建index.ts文件，文件内容如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory, RouteRecordRaw &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;

<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"index"</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../pages/index.vue"</span>),
        <span class="hljs-attr">children</span>: [
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">"/demoTable"</span>,
                <span class="hljs-attr">name</span>: <span class="hljs-string">"demoTable"</span>,
                <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../pages/demo-table/list.vue"</span>)
            &#125;
        ]
    &#125;
]

<span class="hljs-keyword">const</span> router = createRouter(&#123;
    <span class="hljs-attr">history</span>: createWebHashHistory(),
    routes,
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.ts文件中做修改</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>

createApp(App)
    .use(router)
    .mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">引用eslint</h3>
<h5 data-id="heading-3">1.引入eslint及相关的插件</h5>
<pre><code class="hljs language-js copyable" lang="js">npm i typescript eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>eslint： ESlint的核心代码</li>
<li>@typescript-eslint/parser：ESlint的解析器，用于解析typescript，从而检查和规范typescript代码</li>
<li>@typescript-eslint/eslint-plugin：Eslint插件，包含了各类定义好的检测TS代码的规范</li>
</ul>
<h5 data-id="heading-4">2.引入Prettier</h5>
<pre><code class="hljs language-js copyable" lang="js">npm i prettier eslint-config-prettier eslint-plugin-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>prettier：prettier的核心代码</li>
<li>eslint-config-prettier：解决ESlint中的样式规范和prettier中样式规范的冲突，以prettier的样式规范为准，使用ESlint中的样式规范自动失效</li>
<li>eslint-plugin-prettier：将prettier做为ESlint规范来使用</li>
</ul>
<h3 data-id="heading-5">.eslintrc.js配置</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 此项是用来告诉eslint找当前配置文件不能往父级查找</span>
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>, 
  <span class="hljs-comment">// 全局环境</span>
  <span class="hljs-attr">env</span>: &#123;
      <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-comment">// 指定如何解析语法。可以为空，但若不为空，只能配该值</span>
  <span class="hljs-attr">parser</span>: <span class="hljs-string">'vue-eslint-parser'</span>,
  <span class="hljs-comment">// 优先级低于parse的语法解析配置</span>
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-comment">// 指定ESlint的解析器</span>
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
    <span class="hljs-comment">// 允许使用ES语法</span>
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">2020</span>,
    <span class="hljs-comment">// 允许使用import</span>
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>,
    <span class="hljs-comment">// 允许解析JSX</span>
    <span class="hljs-attr">ecmaFeatures</span>: &#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
    &#125;,
  &#125;,
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">'plugin:vue/vue3-essential'</span>,
    <span class="hljs-string">'plugin:@typescript-eslint/recommended'</span>,
    <span class="hljs-string">'prettier'</span>,
  ],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'vue/no-multiple-template-root'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'array-bracket-spacing'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'never'</span>], <span class="hljs-comment">// 是否允许非空数组里面有多余的空格</span>
    <span class="hljs-string">'arrow-parens'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 箭头函数用小括号括起来</span>
    <span class="hljs-string">'block-spacing'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// =>的前/后括号</span>
    <span class="hljs-string">'accessor-pairs'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 在对象中使用getter/setter</span>
    <span class="hljs-string">'block-scoped-var'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 块语句中使用var</span>
    <span class="hljs-string">'brace-style'</span>: [<span class="hljs-string">'warn'</span>, <span class="hljs-string">'1tabs'</span>], <span class="hljs-comment">// 大括号风格</span>
    <span class="hljs-string">'callback-return'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 避免多次调用回调什么的</span>
    <span class="hljs-string">'camelcase'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 强制驼峰法命名</span>
    <span class="hljs-string">'comma-dangle'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'never'</span>], <span class="hljs-comment">// 对象字面量项尾不能有逗号</span>
    <span class="hljs-string">'comma-spacing'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 逗号前后的空格</span>
    <span class="hljs-string">'comma-style'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'last'</span>], <span class="hljs-comment">// 逗号风格，换行时在行首还是行尾</span>
    <span class="hljs-string">'complexity'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-number">11</span>], <span class="hljs-comment">// 循环复杂度</span>
    <span class="hljs-string">'computed-property-spacing'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'never'</span>], <span class="hljs-comment">// 是否允许计算后的键名什么的</span>
    <span class="hljs-string">'consistent-return'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// return 后面是否允许省略</span>
    <span class="hljs-string">'consistent-this'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'that'</span>], <span class="hljs-comment">// this别名</span>
    <span class="hljs-string">'constructor-super'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 非派生类不能调用super，派生类必须调用super</span>
    <span class="hljs-string">'curly'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'all'</span>], <span class="hljs-comment">// 必须使用 if()&#123;&#125; 中的&#123;&#125;</span>
    <span class="hljs-string">'default-case'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// switch语句最后必须有default</span>
    <span class="hljs-string">'dot-location'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 对象访问符的位置，换行的时候在行首还是行尾</span>
    <span class="hljs-string">'dot-notation'</span>: [<span class="hljs-string">'off'</span>, &#123; <span class="hljs-string">'allowKeywords'</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 避免不必要的方括号</span>
    <span class="hljs-string">'eol-last'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 文件以单一的换行符结束</span>
    <span class="hljs-string">'eqeqeq'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 要求使用 === 和 !==</span>
    <span class="hljs-string">'func-names'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 函数表达式必须有名字</span>
    <span class="hljs-string">'func-style'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'declaration'</span>], <span class="hljs-comment">// 函数风格，规定只能使用函数声明/函数表达式</span>
    <span class="hljs-string">'generator-star-spacing'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 生成器函数*的前后空格</span>
    <span class="hljs-string">'guard-for-in'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// for in循环要用if语句过滤</span>
    <span class="hljs-string">'handle-callback-err'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// nodejs 处理错误</span>
    <span class="hljs-string">'id-length'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 变量名长度</span>
    <span class="hljs-string">'indent'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-number">4</span>], <span class="hljs-comment">// 缩进风格</span>
    <span class="hljs-string">'init-declarations'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 声明时必须赋初始值</span>
    <span class="hljs-string">'key-spacing'</span>: [<span class="hljs-string">'off'</span>, &#123; <span class="hljs-string">'beforeColon'</span>: <span class="hljs-literal">false</span>, <span class="hljs-string">'afterColon'</span>: <span class="hljs-literal">true</span> &#125;], <span class="hljs-comment">// 对象字面量中冒号的前后空格</span>
    <span class="hljs-string">'lines-around-comment'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 行前/行后备注</span>
    <span class="hljs-string">'max-depth'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-number">4</span>], <span class="hljs-comment">// 嵌套块深度</span>
    <span class="hljs-string">'max-len'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-number">80</span>, <span class="hljs-number">4</span>], <span class="hljs-comment">// 字符串最大长度</span>
    <span class="hljs-string">'max-nested-callbacks'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'error'</span>], <span class="hljs-comment">// 回调嵌套深度</span>
    <span class="hljs-string">'max-params'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-number">3</span>], <span class="hljs-comment">// 函数最多只能有3个参数</span>
    <span class="hljs-string">'max-statements'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-number">10</span>], <span class="hljs-comment">// 函数内最多有几个声明</span>
    <span class="hljs-string">'new-cap'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 函数名首行大写必须使用new方式调用，首行小写必须用不带new方式调用</span>
    <span class="hljs-string">'new-parens'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// new时必须加小括号</span>
    <span class="hljs-string">'newline-after-var'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 变量声明后是否需要空一行</span>
    <span class="hljs-string">'no-alert'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用alert confirm prompt</span>
    <span class="hljs-string">'no-array-constructor'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用数组构造器</span>
    <span class="hljs-string">'no-bitwise'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用按位运算符</span>
    <span class="hljs-string">'no-caller'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止使用arguments.caller或arguments.callee</span>
    <span class="hljs-string">'no-catch-shadow'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止catch子句参数与外部作用域变量同名</span>
    <span class="hljs-string">'no-class-assign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止给类赋值</span>
    <span class="hljs-string">'no-cond-assign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止在条件表达式中使用赋值语句</span>
    <span class="hljs-string">'no-console'</span>: process.env.NODE_ENV === <span class="hljs-string">'production'</span> ? <span class="hljs-string">'warn'</span> : <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 是否使用 console</span>
    <span class="hljs-string">'no-const-assign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止修改const声明的变量</span>
    <span class="hljs-string">'no-constant-condition'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止在条件中使用常量表达式 if(true) if('warn')</span>
    <span class="hljs-string">'no-continue'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用continue</span>
    <span class="hljs-string">'no-control-regex'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止在正则表达式中使用控制字符</span>
    <span class="hljs-string">'no-debugger'</span>: process.env.NODE_ENV === <span class="hljs-string">'production'</span> ? <span class="hljs-string">'warn'</span> : <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 是否使用 debugger</span>
    <span class="hljs-string">'no-delete-var'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能对var声明的变量使用delete操作符</span>
    <span class="hljs-string">'no-div-regex'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 不能使用看起来像除法的正则表达式/=foo/</span>
    <span class="hljs-string">'no-dupe-keys'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 在创建对象字面量时不允许键重复 &#123;a:'warn',a:'warn'&#125;</span>
    <span class="hljs-string">'no-dupe-args'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 函数参数不能重复</span>
    <span class="hljs-string">'no-duplicate-case'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// switch中的case标签不能重复</span>
    <span class="hljs-string">'no-else-return'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 如果if语句里面有return,后面不能跟else语句</span>
    <span class="hljs-string">'no-empty'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 块语句中的内容不能为空</span>
    <span class="hljs-string">'no-empty-character-class'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 正则表达式中的[]内容不能为空</span>
    <span class="hljs-string">'no-empty-label'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用空label</span>
    <span class="hljs-string">'no-eq-null'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止对null使用==或!=运算符</span>
    <span class="hljs-string">'no-eval'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止使用eval</span>
    <span class="hljs-string">'no-ex-assign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止给catch语句中的异常参数赋值</span>
    <span class="hljs-string">'no-extend-native'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止扩展native对象</span>
    <span class="hljs-string">'no-extra-bind'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止不必要的函数绑定</span>
    <span class="hljs-string">'no-extra-boolean-cast'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止不必要的bool转换</span>
    <span class="hljs-string">'no-extra-parens'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止非必要的括号</span>
    <span class="hljs-string">'no-extra-semi'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止多余的冒号</span>
    <span class="hljs-string">'no-fallthrough'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止switch穿透</span>
    <span class="hljs-string">'no-floating-decimal'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止省略浮点数中的'off' .5 3.</span>
    <span class="hljs-string">'no-func-assign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止重复的函数声明</span>
    <span class="hljs-string">'no-implicit-coercion'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止隐式转换</span>
    <span class="hljs-string">'no-implied-eval'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用隐式eval</span>
    <span class="hljs-string">'no-inline-comments'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止行内备注</span>
    <span class="hljs-string">'no-inner-declarations'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'functions'</span>], <span class="hljs-comment">// 禁止在块语句中使用声明（变量或函数）</span>
    <span class="hljs-string">'no-invalid-regexp'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止无效的正则表达式</span>
    <span class="hljs-string">'no-invalid-this'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止无效的this，只能用在构造器，类，对象字面量</span>
    <span class="hljs-string">'no-irregular-whitespace'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能有不规则的空格</span>
    <span class="hljs-string">'no-iterator'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用__iterator__ 属性</span>
    <span class="hljs-string">'no-label-var'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// label名不能与var声明的变量名相同</span>
    <span class="hljs-string">'no-labels'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止标签声明</span>
    <span class="hljs-string">'no-lone-blocks'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止不必要的嵌套块</span>
    <span class="hljs-string">'no-lonely-if'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止else语句内只有if语句</span>
    <span class="hljs-string">'no-loop-func'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止在循环中使用函数（如果没有引用外部变量不形成闭包就可以）</span>
    <span class="hljs-string">'no-mixed-requires'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-literal">false</span>], <span class="hljs-comment">// 声明时不能混用声明类型</span>
    <span class="hljs-string">'no-mixed-spaces-and-tabs'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-literal">false</span>], <span class="hljs-comment">// 禁止混用tab和空格</span>
    <span class="hljs-string">'linebreak-style'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'windows'</span>], <span class="hljs-comment">// 换行风格</span>
    <span class="hljs-string">'no-multi-spaces'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 不能用多余的空格</span>
    <span class="hljs-string">'no-multi-str'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 字符串不能用\换行</span>
    <span class="hljs-string">'no-multiple-empty-lines'</span>: [<span class="hljs-string">'warn'</span>, &#123;<span class="hljs-string">'max'</span>: <span class="hljs-string">'error'</span>&#125;], <span class="hljs-comment">// 空行最多不能超过'error'行</span>
    <span class="hljs-string">'no-native-reassign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能重写native对象</span>
    <span class="hljs-string">'no-negated-in-lhs'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// in 操作符的左边不能有!</span>
    <span class="hljs-string">'no-nested-ternary'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用嵌套的三目运算</span>
    <span class="hljs-string">'no-new'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止在使用new构造一个实例后不赋值</span>
    <span class="hljs-string">'no-new-func'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 禁止使用new Function</span>
    <span class="hljs-string">'no-new-object'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用new Object()</span>
    <span class="hljs-string">'no-new-require'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用new require</span>
    <span class="hljs-string">'no-new-wrappers'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用new创建包装实例，new String new Boolean new Number</span>
    <span class="hljs-string">'no-obj-calls'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能调用内置的全局对象，比如Math() JSON()</span>
    <span class="hljs-string">'no-octal'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用八进制数字</span>
    <span class="hljs-string">'no-octal-escape'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用八进制转义序列</span>
    <span class="hljs-string">'no-param-reassign'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止给参数重新赋值</span>
    <span class="hljs-string">'no-path-concat'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// node中不能使用__dirname或__filename做路径拼接</span>
    <span class="hljs-string">'no-plusplus'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用++，--</span>
    <span class="hljs-string">'no-process-env'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用process.env</span>
    <span class="hljs-string">'no-process-exit'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用process.exit()</span>
    <span class="hljs-string">'no-proto'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止使用__proto__属性</span>
    <span class="hljs-string">'no-redeclare'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止重复声明变量</span>
    <span class="hljs-string">'no-regex-spaces'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止在正则表达式字面量中使用多个空格 /foo bar/</span>
    <span class="hljs-string">'no-restricted-modules'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 如果禁用了指定模块，使用就会报错</span>
    <span class="hljs-string">'no-return-assign'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// return 语句中不能有赋值表达式</span>
    <span class="hljs-string">'no-script-url'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用javascript:void('off')</span>
    <span class="hljs-string">'no-self-compare'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能比较自身</span>
    <span class="hljs-string">'no-sequences'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用逗号运算符</span>
    <span class="hljs-string">'no-shadow'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 外部作用域中的变量不能与它所包含的作用域中的变量或参数同名</span>
    <span class="hljs-string">'no-shadow-restricted-names'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 严格模式中规定的限制标识符不能作为声明时的变量名使用</span>
    <span class="hljs-string">'no-spaced-func'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 函数调用时 函数名与()之间不能有空格</span>
    <span class="hljs-string">'no-sparse-arrays'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止稀疏数组， ['warn',,'error']</span>
    <span class="hljs-string">'no-sync'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// nodejs 禁止同步方法</span>
    <span class="hljs-string">'no-ternary'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁止使用三目运算符</span>
    <span class="hljs-string">'no-trailing-spaces'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 一行结束后面不要有空格</span>
    <span class="hljs-string">'no-this-before-super'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 在调用super()之前不能使用this或super</span>
    <span class="hljs-string">'no-throw-literal'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止抛出字面量错误 throw 'error';</span>
    <span class="hljs-string">'no-undef'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 不能有未定义的变量</span>
    <span class="hljs-string">'no-undef-init'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 变量初始化时不能直接给它赋值为undefined</span>
    <span class="hljs-string">'no-undefined'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能使用undefined</span>
    <span class="hljs-string">'no-unexpected-multiline'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 避免多行表达式</span>
    <span class="hljs-string">'no-underscore-dangle'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 标识符不能以_开头或结尾</span>
    <span class="hljs-string">'no-unneeded-ternary'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止不必要的嵌套 var isYes = answer === 'warn' ? true : false;</span>
    <span class="hljs-string">'no-unreachable'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 不能有无法执行的代码</span>
    <span class="hljs-string">'no-unused-expressions'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止无用的表达式</span>
    <span class="hljs-string">'no-unused-vars'</span>: [<span class="hljs-string">'error'</span>, &#123;<span class="hljs-string">'vars'</span>: <span class="hljs-string">'all'</span>, <span class="hljs-string">'args'</span>: <span class="hljs-string">'after-used'</span>&#125;], <span class="hljs-comment">// 不能有声明后未被使用的变量或参数</span>
    <span class="hljs-string">'no-use-before-define'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 未定义前不能使用</span>
    <span class="hljs-string">'no-useless-call'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止不必要的call和apply</span>
    <span class="hljs-string">'no-void'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁用void操作符</span>
    <span class="hljs-string">'no-var'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 禁用var，用let和const代替</span>
    <span class="hljs-string">'no-warning-comments'</span>: [<span class="hljs-string">'warn'</span>, &#123; <span class="hljs-string">'terms'</span>: [<span class="hljs-string">'todo'</span>, <span class="hljs-string">'fixme'</span>, <span class="hljs-string">'xxx'</span>], <span class="hljs-string">'location'</span>: <span class="hljs-string">'start'</span> &#125;], <span class="hljs-comment">// 不能有警告备注</span>
    <span class="hljs-string">'no-with'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁用with</span>
    <span class="hljs-string">'object-curly-spacing'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'never'</span>], <span class="hljs-comment">// 大括号内是否允许不必要的空格</span>
    <span class="hljs-string">'object-shorthand'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 强制对象字面量缩写语法</span>
    <span class="hljs-string">'one-var'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 连续声明</span>
    <span class="hljs-string">'operator-assignment'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// 赋值运算符 += -=什么的</span>
    <span class="hljs-string">'operator-linebreak'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'after'</span>], <span class="hljs-comment">// 换行时运算符在行尾还是行首</span>
    <span class="hljs-string">'padded-blocks'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 块语句内行首行尾是否要空行</span>
    <span class="hljs-string">'prefer-const'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 首选const</span>
    <span class="hljs-string">'prefer-spread'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 首选展开运算</span>
    <span class="hljs-string">'prefer-reflect'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 首选Reflect的方法</span>
    <span class="hljs-string">'quotes'</span>: [<span class="hljs-string">'warn'</span>, <span class="hljs-string">'single'</span>], <span class="hljs-comment">// 引号类型 `` '' ''</span>
    <span class="hljs-string">'quote-props'</span>:[<span class="hljs-string">'error'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// 对象字面量中的属性名是否强制双引号</span>
    <span class="hljs-string">'radix'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// parseInt必须指定第二个参数</span>
    <span class="hljs-string">'id-match'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 命名检测</span>
    <span class="hljs-string">'require-yield'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 生成器函数必须有yield</span>
    <span class="hljs-string">'semi'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// 语句强制分号结尾</span>
    <span class="hljs-string">'semi-spacing'</span>: [<span class="hljs-string">'off'</span>, &#123;<span class="hljs-string">'before'</span>: <span class="hljs-literal">false</span>, <span class="hljs-string">'after'</span>: <span class="hljs-literal">true</span>&#125;], <span class="hljs-comment">// 分号前后空格</span>
    <span class="hljs-string">'sort-vars'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 变量声明时排序</span>
    <span class="hljs-string">'space-after-keywords'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// 关键字后面是否要空一格</span>
    <span class="hljs-string">'space-before-blocks'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// 不以新行开始的块&#123;前面要不要有空格</span>
    <span class="hljs-string">'space-before-function-paren'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'always'</span>], <span class="hljs-comment">// 函数定义时括号前面要不要有空格</span>
    <span class="hljs-string">'space-in-parens'</span>: [<span class="hljs-string">'off'</span>, <span class="hljs-string">'never'</span>], <span class="hljs-comment">// 小括号里面要不要有空格</span>
    <span class="hljs-string">'space-infix-ops'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 中缀操作符周围要不要有空格</span>
    <span class="hljs-string">'space-return-throw-case'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// return throw case后面要不要加空格</span>
    <span class="hljs-string">'space-unary-ops'</span>: [<span class="hljs-string">'off'</span>, &#123; <span class="hljs-string">'words'</span>: <span class="hljs-literal">true</span>, <span class="hljs-string">'nonwords'</span>: <span class="hljs-literal">false</span> &#125;], <span class="hljs-comment">// 一元运算符的前/后要不要加空格</span>
    <span class="hljs-string">'spaced-comment'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 注释风格要不要有空格什么的</span>
    <span class="hljs-string">'strict'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 使用严格模式</span>
    <span class="hljs-string">'use-isnan'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止比较时使用NaN，只能用isNaN()</span>
    <span class="hljs-string">'valid-jsdoc'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// jsdoc规则</span>
    <span class="hljs-string">'valid-typeof'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 必须使用合法的typeof的值</span>
    <span class="hljs-string">'vars-on-top'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// var必须放在作用域顶部</span>
    <span class="hljs-string">'vue/require-v-for-key'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// vue的for循环是否必须有key</span>
    <span class="hljs-string">'wrap-iife'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'inside'</span>], <span class="hljs-comment">// 立即执行函数表达式的小括号风格</span>
    <span class="hljs-string">'wrap-regex'</span>: <span class="hljs-string">'off'</span>, <span class="hljs-comment">// 正则表达式字面量用小括号包起来</span>
    <span class="hljs-string">'yoda'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'never'</span>] <span class="hljs-comment">// 禁止尤达条件</span>
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">npm指令</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"script"</span>: &#123;
    <span class="hljs-string">"lint"</span>: <span class="hljs-string">"vue-cli-service lint"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目格式化一次，打包项目前也格式化一次。保存最后的代码都被格式化过</p>
<h3 data-id="heading-7">.prettierrc配置</h3>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"printWidth"</span>: <span class="hljs-number">80</span>, <span class="hljs-comment">// 单行输出（不折行）的（最大）长度</span>
  <span class="hljs-string">"useTabs"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 不使用缩进符，而使用空格</span>
  <span class="hljs-string">"tabWidth"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 每个缩进的空格数</span>
  <span class="hljs-string">"tabs"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 使用制表符 (tab) 缩进行而不是空格 (space)</span>
  <span class="hljs-string">"semi"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否在语句末尾打印分号</span>
  <span class="hljs-string">"singleQuote"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否使用单引号</span>
  <span class="hljs-comment">// "quoteProps": "as-needed", // 尽在需要时在对象属性周围添加引号</span>
  <span class="hljs-string">"quoteProps"</span>: <span class="hljs-string">"consistent"</span>,
  <span class="hljs-string">"trailingComma"</span>: <span class="hljs-string">"all"</span>, <span class="hljs-comment">// 去除对象最末尾元素跟随的逗号</span>
  <span class="hljs-string">"arrowParens"</span>: <span class="hljs-string">"always"</span>, <span class="hljs-comment">// 箭头函数，只有一个参数的时候，也需要括号</span>
  <span class="hljs-string">"rangeStart"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 每个文件格式化的范围是文件的全部内容</span>
  <span class="hljs-string">"proseWrap"</span>: <span class="hljs-string">"always"</span>, <span class="hljs-comment">// 当超出print width（上面有这个参数）时就折行</span>
  <span class="hljs-string">"endOfLine"</span>: <span class="hljs-string">"lf"</span>, <span class="hljs-comment">// 换行符使用 lf</span>
  <span class="hljs-string">"bracketSpacing"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否在对象属性添加空格</span>
  <span class="hljs-string">"jsxBracketSameLine"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 将 > 多行 JSX 元素放在最后一行的末尾，而不是单独放在下一行（不适用于自闭元素）,默认false,这里选择>不另起一行</span>
  <span class="hljs-string">"htmlWhitespaceSensitivity"</span>: <span class="hljs-string">"ignore"</span>, <span class="hljs-comment">// 指定 HTML 文件的全局空白区域敏感度, "ignore" - 空格被认为是不敏感的</span>
  <span class="hljs-string">"jsxSingleQuote"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// jsx 不使用单引号，而使用双引号</span>
  <span class="hljs-string">"rangeStart"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 每个文件格式化的范围是文件的全部内容</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">引入TS</h3>
<pre><code class="hljs language-js copyable" lang="js">npm install typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置tsconfig.json文件</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">"compilerOptions"</span>: &#123;
        <span class="hljs-comment">// 允许从没有设置默认导出的模块中默认导入。这并不影响代码的输出，仅为了类型检查。</span>
        <span class="hljs-string">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 从 tslib 导入辅助工具函数（比如 __extends， __rest等）</span>
        <span class="hljs-string">"importHelpers"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"target"</span>: <span class="hljs-string">"esnext"</span>,
        <span class="hljs-comment">// 指定生成哪个模块系统代码</span>
        <span class="hljs-string">"module"</span>: <span class="hljs-string">"esnext"</span>,
        <span class="hljs-comment">// 决定如何处理模块</span>
        <span class="hljs-string">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,
        <span class="hljs-comment">// 指定ECMAScript目标版本</span>
        <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"jsx"</span>: <span class="hljs-string">"preserve"</span>,
        <span class="hljs-comment">// 生成相应的 .map文件。</span>
        <span class="hljs-string">"sourceMap"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 忽略所有的声明文件（ *.d.ts）的类型检查。</span>
        <span class="hljs-string">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"resolveJsonModule"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 编译过程中需要引入的库文件的列表。</span>
        <span class="hljs-string">"lib"</span>: [<span class="hljs-string">"esnext"</span>, <span class="hljs-string">"dom"</span>],
        <span class="hljs-comment">// 解析非相对模块名的基准目录</span>
        <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"."</span>,
        <span class="hljs-comment">// 模块名到基于 baseUrl的路径映射的列表。</span>
        <span class="hljs-string">"paths"</span>: &#123;
            <span class="hljs-string">"@/*"</span>: [<span class="hljs-string">"src/*"</span>],
            <span class="hljs-string">"#/*"</span>: [<span class="hljs-string">"types/*"</span>]
        &#125;,
        <span class="hljs-comment">// 要包含的类型声明文件名列表</span>
        <span class="hljs-string">"types"</span>: [
            <span class="hljs-comment">// "node",</span>
            <span class="hljs-string">"vite/client"</span>
        ],
        <span class="hljs-string">"typeRoots"</span>: [<span class="hljs-string">"./node_modules/@types/"</span>, <span class="hljs-string">"./types"</span>]
    &#125;,
    <span class="hljs-string">"include"</span>: [<span class="hljs-string">"src/**/*.ts"</span>, <span class="hljs-string">"src/**/*.d.ts"</span>, <span class="hljs-string">"src/**/*.tsx"</span>, <span class="hljs-string">"src/**/*.vue"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js修改为main.ts</p>
<h3 data-id="heading-9">引入element（vite）</h3>
<pre><code class="hljs language-js copyable" lang="js">npm install vite-plugin-style-<span class="hljs-keyword">import</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照官网修改配置</p>
<h3 data-id="heading-10">问题记录</h3>
<p>1.main.ts 中，提示import App from './App.vue'处，找不到 App.vue 这个模块
解决方案：
1、将 shims-vue.d.ts 文件一分为二</p>
<p>2、在 shims-vue.d.ts 文件同级目录下新建 vue.d.ts（名字不一定叫 vue，如 xxx.d.ts 也可以），然后此文件包含代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.d.ts</span>
declare <span class="hljs-built_in">module</span> <span class="hljs-string">'*.vue'</span> &#123;
  <span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// shims-vue.d.ts</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter, &#123; Route &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> &#123; Store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

declare <span class="hljs-built_in">module</span> <span class="hljs-string">'vue/types/vue'</span> &#123;
  interface Vue &#123;
    <span class="hljs-attr">$router</span>: VueRouter;
    $route: Route;
    $store: Store<any>;
    <span class="hljs-comment">// 以下是在main.ts中挂载到Vue.prototype上的变量</span>
    $api: any;
    $mock: any;
    $configs: any;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>资料参考：</p>
<p><a href="https://blog.csdn.net/fu983531588/article/details/109333898" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/fu983531588…</a>
<a href="https://juejin.cn/post/6844904113822498830" target="_blank">juejin.cn/post/684490…</a></p></div>  
</div>
            