
---
title: '哈，我终于会用npm把自己造的轮子发布出去了！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129975db7f84448eaa32304c348a6a6a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 01:06:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129975db7f84448eaa32304c348a6a6a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">被迫学习的原因</h1>
<pre><code class="copyable">嗯，由于生活所迫，我在一家很奇怪的部门工作，我们的项目好像很多，但是其实。。。。。 
有一天，大佬奇思妙想，觉得我们的这些小项目也应该被做成公共的，于是，便有了事件的起因。
所以，大佬让我这个小菜鸡去学习把造的轮子发布到npm里面，方便后面的项目使用。

于是，我开始了埋头苦干。
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">过程与结果</h1>
<pre><code class="copyable">第一步，拿到需求就是一顿搜索，嗯，搜了一堆，基本都看了一下，然后整理，最后结束，成功！

我的项目整体是这样的结构：
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129975db7f84448eaa32304c348a6a6a~tplv-k3u1fbpfcp-watermark.image" alt="npms.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">我的项目使用 “vue init webpack-simple” 命令初始化一个vue项目后进行修改的
（主要修改的文件在图中有标注）
其中，我的公共组件放在了components中，这里模仿了elementui的文件结构，文件名就是我的组件名字
我的例子组件内容是：
1. ExampleComponent：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
  <div>
    例子组件
    &#123;&#123; msg &#125;&#125;
    <ul>
      <li
        v-for="(item, index) in propArr"
        :key="index"
        @click="clickEvent(item)"
      >
        &#123;&#123; item.name &#125;&#125;
      </li>
    </ul>
  </div>
</template>

<script>
export default &#123;
  name: 'ExampleComponent',  // 组件名字
  props: &#123;
    msg: &#123;
      type: String,
      default: 'Hello shishi' // 默认值
    &#125;,
    propArr: &#123;
      type: Array,
      required: true // 必传字段
    &#125;
  &#125;,
  data () &#123;
    return &#123;

    &#125;
  &#125;,
  created () &#123;

  &#125;,
  mounted () &#123;

  &#125;,
  methods: &#123;
    clickEvent (val) &#123; // 暴漏点击事件
      this.$emit('clickEvent', val)
    &#125;
  &#125;
&#125;
</script>

<style scoped>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">2. exampleComponents的index.js文件的内容是：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import ExampleComponent from './src/ExampleComponent.vue'
import _Vue from 'vue'
/* istanbul ignore next */
ExampleComponent.install = function(Vue) &#123;
  if (!Vue) &#123;
    window.Vue = Vue = _Vue
    &#125;
  Vue.component(ExampleComponent.name, ExampleComponent)
&#125;

export default ExampleComponent
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">3. 在最外层的index.js的配置：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import ExampleComponent from './src/components/exampleComponent/index.js'
import First from './src/components/first/index.js'

const components = [ First, ExampleComponent]
const install = (Vue, opts = &#123;&#125;) => &#123;
  components.forEach(component => &#123;
    console.log(component)
    Vue.component(component.name, component)
  &#125;)
&#125;
if (typeof window !== 'undefined' && window.Vue) &#123;
  install(window.Vue)
&#125;
export default &#123;
  install,
  First,
  ExampleComponent
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">4.webpack.config.js (webpack主要修改了 output ， 的内容)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var path = require('path')
var webpack = require('webpack')
const NODE_ENV = process.env.NODE_ENV

module.exports = &#123;
  entry: NODE_ENV == 'development' ? './src/main.js' : './index.js',
  output: &#123;
    path: path.resolve(__dirname, './dist'),
    publicPath: '/dist/',
    filename: 'sjy-tool-components.js',
    library: 'sjy-tool-components', // 指定的就是你使用require时的模块名
    libraryTarget: 'umd',// 指定输出格式
    umdNamedDefine: true // 会对 UMD 的构建过程中的 AMD 模块进行命名。否则就使用匿名的 define
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      &#125;,
      &#123;
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader'
        ],
      &#125;,
      &#123;
        test: /\.sass$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader?indentedSyntax'
        ],
      &#125;,
      &#123;
        test: /\.vue$/,
        loader: 'vue-loader',
        options: &#123;
          loaders: &#123;
            js: 'babel-loader',
            // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
            // the "scss" and "sass" values for the lang attribute to the right configs here.
            // other preprocessors should work out of the box, no loader config like this necessary.
            'scss': [
              'vue-style-loader',
              'css-loader',
              'sass-loader'
            ],
            'sass': [
              'vue-style-loader',
              'css-loader',
              'sass-loader?indentedSyntax'
            ]
          &#125;
          // other vue-loader options go here
        &#125;
      &#125;,
      &#123;
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      &#125;,
      &#123;
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: &#123;
          name: '[name].[ext]?[hash]'
        &#125;
      &#125;
    ]
  &#125;,
  resolve: &#123;
    alias: &#123;
      'vue$': 'vue/dist/vue.esm.js'
    &#125;,
    extensions: ['*', '.js', '.vue', '.json']
  &#125;,
  devServer: &#123;
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  &#125;,
  performance: &#123;
    hints: false
  &#125;
&#125;

if (process.env.NODE_ENV === 'production') &#123;
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin(&#123;
      'process.env': &#123;
        NODE_ENV: '"production"'
      &#125;
    &#125;),
    new webpack.optimize.UglifyJsPlugin(&#123;
      sourceMap: true,
      compress: &#123;
        warnings: false
      &#125;
    &#125;),
    new webpack.LoaderOptionsPlugin(&#123;
      minimize: true
    &#125;)
  ])
&#125;else &#123;
  module.exports.devtool = '#eval-source-map'
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">5.package.json(主要修改如图，private改为false，main的路径变化)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/128e015635f94a5cb0f3ed967d4d47ba~tplv-k3u1fbpfcp-watermark.image" alt="WeChat Image_20210701164249.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">6.index.html(修改引用路径)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52a8e9ecdc054c7a9e7a0daaeb6c0973~tplv-k3u1fbpfcp-watermark.image" alt="WeChat Screenshot_20210701164427.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">   然后就结束咯，可以npm发布咯，当然首先要有一个npm的账号呀，https://www.npmjs.com/ 官网注册一个咯

   7.发布
   npm adduser 添加用户，
   npm login 登录
   npm publish 发布
   
   
   
   npm unpublish XXXX@1.0 --force 删除已发布的
   
   8.使用
   正常流程  npm i sjy-tool-components
   
   **新的项目里在main里面引用**
   
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import SjyToolComponent from 'sjy-tool-components'
Vue.use(SjyToolComponents)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">再组件里直接引用即可咯
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/267a47d0489240bf8fee0420efa7b436~tplv-k3u1fbpfcp-watermark.image" alt="WeChat Screenshot_20210701165138.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">   至此，我的梳理结束咯，我的demo的地址附上https://github.com/shijiayu0818/sjy-tool-components.git
   
   哈哈，第一次在掘金不是摸鱼，而是一本正经的做一下自己的收获。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f417ee5d4d04ef390d9478a26977b52~tplv-k3u1fbpfcp-watermark.image" alt="WeChat Image_20210701170236.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            