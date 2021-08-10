
---
title: 'vue3+ts项目搭建和封装（上篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bd525cf61954e1986fdc34019b766ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 15:47:29 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bd525cf61954e1986fdc34019b766ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h3 data-id="heading-0">1. 首先，要确保自己的node版本 >= 12.0.0, 在命令行执行<code>node-v</code>就可以查看node版本</h3>
<p>如果node版本低于12的话，就...</p>
<pre><code class="copyable">node有一个模块叫n，是专门用来管理node.js的版本的。
第一步：首先安装n模块：
npm install -g n

第二步：升级node倒最新稳定版
n stable
(n后面也可以跟版本号)
n v14.15.1
或者
n 14.15.1

## 就完事儿了
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 开始搭建项目</h3>
<p>首先进入需要创建项目的路径下</p>
<p>使用npm： <code>npm init @vitejs/app xxx</code>  xxx是项目名</p>
<p>使用yarn：<code>yarn create @vitejs/app xxx</code> xxx是项目名</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bd525cf61954e1986fdc34019b766ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后:</p>
<pre><code class="copyable">? Project name: enter
? Select a template: ...   vue
? Select a variant: vue-ts

##就完事儿了
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到一个干干净净的vue3.0 + typescript项目了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20589027b7484e8991415070b97c4887~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">前端技术框架部分</h4>
<p>这里用到了<code>vuex4.0</code>,<code>vue-router4.0</code>,<code>axios</code>,<code>element-plus</code>和<code>vite</code></p>
<blockquote>
<p>npm install vuex@next vue-router@next -S axios element-plus vite</p>
</blockquote>
<p>还有sass</p>
<blockquote>
<p>npm install sass --D</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37d6988960e24584a728ea3981fbd38a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">配置项目</h2>
<p>用vite创建初始vue项目后，会生成一个默认的<code>vite.config.ts</code>文件，内容如下：</p>
<pre><code class="copyable">import &#123; defineConfig &#125; from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig(&#123;
  plugins: [vue()]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>然后我们开始配置vite.config.ts， 并且会在代码中以注释的形式进行说明</p>
</blockquote>
<pre><code class="copyable">// 使用 defineConfig 帮手函数，这样不用 jsdoc 注解也可以获取类型提示
import &#123; defineConfig &#125; from "vite"
import vue from "@vitejs/plugin-vue"
// 此处引用了path路径导向
import path from "path"
// 这里引用了svg-icon，后面会讲解
import &#123; createSvg &#125; from './src/icons/index'
 
export default defineConfig(&#123;
  // 查看 插件 API 获取 Vite 插件的更多细节 https://www.vitejs.net/guide/api-plugin.html
  plugins: [
      vue(),
      // 这里引用了svg-icon，后面会讲解说明
      createSvg('./src/icons/svg/')
  ],
  // 在生产中服务时的基本路径
  base: "./",
  // 配置别名绝对路径  https://webpack.js.org/configuration/resolve/
  resolve: &#123;
  // resolve.alias: 更轻松地为import或require某些模块创建别名
      alias: &#123;
          // 如果报错__dirname找不到，需要安装node,执行npm install @types/node --save-dev
          "@": path.resolve(__dirname, "./src"),
          "@assets": path.resolve(__dirname, "./src/assets"),
          "@components": path.resolve(__dirname, "./src/components"),
          "@views": path.resolve(__dirname, "./src/views"),
          "@store": path.resolve(__dirname, "./src/store"),
      &#125;,
  &#125;,
  // 与根相关的目录，构建输出将放在其中，如果目录存在，它将在构建之前被删除
  // @default 'dist'
  build: &#123;
      outDir: "dist",
  &#125;,
  server: &#123;
      https: false, // 是否开启 https
      open: true, // 是否自动在浏览器打开
      port: 8001, // 端口号
      host: "0.0.0.0",
      // 跨域代理
      proxy: &#123;
          "/api": &#123;
              target: "http://localhost:3000", // 后台接口
              changeOrigin: true,
              // secure: false, // 如果是https接口，需要配置这个参数
              // ws: true, //websocket支持
              // 截取api，并用api代替
              // rewrite: (path) => path.replace(/^\/api/, "/api"),
          &#125;,
      &#125;,
  &#125;,
  // 引入第三方的配置
  optimizeDeps: &#123;
    include: [],
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">tsconfig.json配置</h2>
<p>由于开发包含ts的项目经常要配置tsconfig.json，所以自己梳理了一份tsconfig.json文件；<br>
里面包含了一些常用的tsconfig选项以及注解：</p>
<pre><code class="copyable">&#123;
  "compilerOptions": &#123;
    "allowUnreachableCode": true, // 不报告执行不到的代码错误。
    "allowUnusedLabels": false,// 不报告未使用的标签错误
    "alwaysStrict": false, // 以严格模式解析并为每个源文件生成 "use strict"语句
    "experimentalDecorators": true, // 启用实验性的ES装饰器
    "noImplicitAny": false, // 是否默认禁用 any
    "removeComments": true, // 是否移除注释
    "target": "esnext",// 编译的目标是什么版本的
    "module": "esnext", // "commonjs" 指定生成哪个模块系统代码
    "strict": true,
    "jsx": "preserve",  // 在 .tsx文件里支持JSX
    "importHelpers": true,
    "moduleResolution": "node",
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "suppressImplicitAnyIndexErrors": true,
    "sourceMap": true,  // 是否生成map文件
    "baseUrl": ".", // 工作根目录
    // "outDir": "./dist", // 输出目录
    "declaration": true, // 是否自动创建类型声明文件
    "declarationDir": "./lib", // 类型声明文件的输出目录
    "allowJs": true, // 允许编译javascript文件。
    "types": [
      "webpack-env",
      "node"
    ], //指定引入的类型声明文件，默认是自动引入所有声明文件，一旦指定该选项，则会禁用自动引入，改为只引入指定的类型声明文件，如果指定空数组[]则不引用任何文件
    "paths": &#123;  // 指定模块的路径，和baseUrl有关联，和webpack中resolve.alias配置一样
      "@/*": ["src/*"],
      "@assets/*": ["src/assets/*"],
      "@components/*": ["src/components/*"],
      "@views/*": ["src/views/*"],
      "@store/*": ["src/store/*"],
    &#125;,
    "lib": [// 编译过程中需要引入的库文件的列表
      "es5",
      "es2015",
      "es2016",
      "es2017",
      "es2018",
      "esnext",
      "dom",
      "dom.iterable",
      "scripthost"
    ]
  &#125;,
   // 指定一个匹配列表（属于自动指定该路径下的所有ts相关文件）
  "include": [
    "src/**/*.ts",
    "src/**/*.tsx",
    "src/**/*.vue"
  ],
  "exclude": [
    "node_modules",
    "src/assets/json/*.json",
    "src/assets/css/*.scss"
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">svg-icon的配置</h2>
<h3 data-id="heading-6">1. 首先引入svg插件</h3>
<pre><code class="copyable">yarn add svg-sprite-loader -D
// 或者
npm install svg-sprite-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fc483d5bb040eca1683d93be835af5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">2. 创建文件</h3>
<p>在<code>@/src</code>里面创建<code>icons</code>文件夹，里面创建<code>index.vue</code>(svgicon的模板文件), <code>index.ts</code>(svgicon的js逻辑), <code>svg文件夹</code>(svg图标存放的地址)</p>
<h4 data-id="heading-8">index.vue(svgicon的模板文件)</h4>
<p>这部分需要用到fs模块，所以需要：</p>
<pre><code class="copyable">yarn add fs
// 或者
npm install fs
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
    <svg :class="svgClass" v-bind="$attrs" :style="&#123; color: color &#125;">
        <use :xlink:href="iconName"></use>
    </svg>
</template>

<script setup lang="ts">
import &#123; computed, defineProps &#125; from 'vue'
const props = defineProps(&#123;
    name: &#123;
        type: String,
        required: true
    &#125;,
    color: &#123;
        type: String,
        default: ''
    &#125;
&#125;)
const iconName = computed(() => `#icon-$&#123; props.name &#125;`)
const svgClass = computed(() => &#123;
    if(props.name) return `svg-icon icon-$&#123; props.name &#125;`
    return 'svg-icon'
&#125;)
</script>

<style scoped>
.svg-icon&#123;width: 1em;height: 1em;fill:currentColor; vertical-align: middle;&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">index.ts(svg的js逻辑文件)</h4>
<blockquote>
<p>这部分有问题的小伙伴可以找我，我写了注释的。</p>
</blockquote>
<pre><code class="copyable">import &#123; readFileSync, readdirSync &#125; from 'fs'

let idPerfix = ''
const svgTitle = /<svg([^>+].*?)>/
const clearHeightWidth = /(width|height)="([^>+].*?)"/g
const hasViewBox = /(viewBox="[^>+].*?")/g
const clearReturn = /(\r)|(\n)/g

// 查找svg文件
function svgFind(e) &#123;
  const arr = []
  const dirents = readdirSync(e, &#123; withFileTypes: true &#125;)
  for (const dirent of dirents) &#123;
    if (dirent.isDirectory()) arr.push(...svgFind(e + dirent.name + '/'))
    else &#123;
        const svg = readFileSync(e + dirent.name)
                    .toString()
                    .replace(clearReturn, '')
                    .replace(svgTitle, ($1, $2) => &#123;
                            let width = 0,
                                height = 0,
                                content = $2.replace(clearHeightWidth, (s1, s2, s3) => &#123;
                                    if (s2 === 'width') width = s3
                                    else if (s2 === 'height') height = s3
                                    return ''
                                &#125;)
                if (!hasViewBox.test($2)) content += `viewBox="0 0 $&#123;width&#125; $&#123;height&#125;"`
                return `<symbol id="$&#123;idPerfix&#125;-$&#123;dirent.name.replace('.svg', '')&#125;" $&#123;content&#125;>`
        &#125;).replace('</svg>', '</symbol>')
        arr.push(svg)
    &#125;
  &#125;
  return arr
&#125;

// 生成svg
export const createSvg = (path: any, perfix = 'icon') => &#123;
  if (path === '') return
  idPerfix = perfix
  const res = svgFind(path)
  return &#123;
    name: 'svg-transform',
    transformIndexHtml(dom: String) &#123;
        return dom.replace(
            '<body>',
            `<body><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position: absolute; width: 0; height: 0">$&#123;res.join('')&#125;</svg>`
        )
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">svg存放svg图标</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/285fd8674756470784b61f87c6f14fc5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">3. 在vite.config.ts里面引用svg</h2>
<pre><code class="copyable">import &#123; defineConfig &#125; from "vite"
import &#123; createSvg &#125; from './src/icons/index'

export default defineConfig(&#123;
    plugins: [
      vue(),
      createSvg('./src/icons/svg/')
     ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4. 在main.ts中写入<code>svg-icon</code>模板</h3>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import App from './App.vue'
import svgIcon from './icons/index.vue'

const app = createApp(App)

app
.component('svg-icon', svgIcon)
.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">酱紫，就可以啦。（用法）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9dfc805d74444f68d1d73f7fbefe82d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>name是svg的名称</li>
<li>color是svg的颜色</li>
</ul>
<h2 data-id="heading-14">最后</h2>
<blockquote>
<p>公众号：小何成长，佛系更文，都是自己曾经踩过的坑或者是学到的东西</p>
<p>有兴趣的小伙伴欢迎关注我哦，我是：<code>何小玍</code>。大家一起进步鸭</p>
</blockquote></div>  
</div>
            