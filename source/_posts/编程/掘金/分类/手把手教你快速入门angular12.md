
---
title: '手把手教你快速入门angular12'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5a34ce3ff3f42ad91d138fc4abf00b3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 02:44:40 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5a34ce3ff3f42ad91d138fc4abf00b3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>该文章主要面向对 angular感兴趣前端童鞋。在国内，大多企业使用的技术栈是vue、react，鲜有公司使用angular，而我恰好用到，故记录并分享。</p>
</blockquote>
<h3 data-id="heading-0">通过这篇文章，你能了解到以下几点：</h3>
<ul>
<li>angular环境配置</li>
<li>开发工具配置</li>
<li>CLI工程结构</li>
<li>工程源码文件结构</li>
<li>项目创建</li>
</ul>
<h4 data-id="heading-1">一、angular环境配置：</h4>
<p>Node => NPM/CNPM => Angular CLI</p>
<ul>
<li>安装node.js是使用npm管理项目依赖的软件包，由于网络原因，可使用cnpm作为替代的包管理工具，使用angular CLI 使我们无需理会复杂的配置，更专注Angular.</li>
<li>安装完毕后，在控制台输入：</li>
</ul>
<pre><code class="copyable">npm install -g @angular/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>查看版本</li>
</ul>
<pre><code class="copyable">angular version
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5a34ce3ff3f42ad91d138fc4abf00b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">二、开发工具配置：</h4>
<ul>
<li>Vscode 的推荐拓展：</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffe3bca253e243b3ae1f28e188416752~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Chrome 的推荐扩展：Angular DevTools</li>
</ul>
<p>方便调试程序，可在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fangular-developer-tools%2Fienfalfjdbdpebioblfackkekamfmbnh" target="_blank" rel="nofollow noopener noreferrer" title="https://chrome.google.com/webstore/detail/angular-developer-tools/ienfalfjdbdpebioblfackkekamfmbnh" ref="nofollow noopener noreferrer">Chrome 网上应用店</a>中找到 Angular DevTools。</p>
<h4 data-id="heading-3">三、CLI工程结构：</h4>
<pre><code class="copyable">| -- myProject
    | -- .editorconfig  // 用于在不同编辑器中统一代码风格
    | -- .gitignore  // git中忽略文件列表
    | -- .README.md  // Markdown格式的说明文件
    | -- .angular.json  // angular 的配置文件
    | -- .browserslistrc  // 配置浏览器兼容的文件
    | -- .karma.conf.js  // 自动化测试框架Karma的配置文件
    | -- .package.json  //  NPM包定义文件
    | -- .package-lock.json  // 依赖包版本锁定文件
    | -- .tsconfig.app.json  // 用于app项目的TypeScript的配置文件
    | -- .tsconfig.spec.json  // 用于测试的TypeScript的配置文件
    | -- .tsconfig.json  //  整个工作区的TypeScript的配置文件
    | -- .tsconfig.spec.json  // 用于测试的TypeScript的配置文件
    | -- .tslint.json  // TypeScript的代码静态扫描配置
    | -- .e2e  // 自动化集成测试项目
    | -- .src  //  源代码目录
            | -- .favicon.ico //  收藏图标
            | -- .index.html //  收藏图标
            | -- .main.ts  //  入口 ts文件
            | -- .polyfill.ts  //  用于不同浏览器兼容版本加载
            | -- .style.css  //  整个项目的全局的css
            | -- .test.ts  //  测试入口
            | -- .app  //  工程源码目录
            | -- .assets //  资源目录
            | -- .environments  //  环境配置
                 | -- .environments.prod.ts  //  生产环境
                 | -- .environments.ts  //  开发环境

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">四、工程源码文件结构</h4>
<h5 data-id="heading-5">1.app目录：</h5>
<p>app目录是要编写的代码目录。在新建项目时命令行已经默认生成出来了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e139b5f31353408793173d4eaf74f8a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">2.app目录中的app.component.ts：</h5>
<p>该文件表示组件，组件是Angular应用的基本构建模块，可理解为一段带有业务逻辑和数据的html</p>
<pre><code class="copyable">
import &#123; Component,&#125; from '@angular/core';

@Component(&#123;
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
&#125;)
export class AppComponent &#123;
 
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们来分析app.component.ts文件中的每一段代码：</p>
<pre><code class="copyable">import &#123;Component&#125; from '@angular/core';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码是从Angular核心模块里面引入了component装饰器</p>
<pre><code class="copyable">@Component(&#123;
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码是用装饰器定义了一个组件以及组件的元数据 所有的组件都必须使用这个装饰器来注解，组件元数据 Angular会通过这里面的属性来渲染组件并执行逻辑</p>
<ul>
<li><code>selector</code> 是一个css选择器。表示该组件可通过<code>app-root</code>的HTML标签来调用，<code>index.html</code>中有个<code><app-root>Loading...</app-root></code>标签，这个标签用来展示该组件的内容。</li>
<li><code>templateUrl </code>指定了一个html文件作为组件的模板，定义了组件的布局和内容。在这里定义<code>app.component.html</code>，最终在<code>index.html</code>中<code><app-root>/<app-root></code>这个标签的内容将展示<code>app.component.html</code>里面的内容。也就是templateUrl所定义的页面定义了用户最终看见的页面的布局和内容。</li>
<li><code>styleUrls </code>指定了一组css文件。可以在这个css中编写这个组件模板要用到的样式。也就是<code>app.component.html</code>和<code>app.component.css</code>两个文件。</li>
</ul>
<pre><code class="copyable">export class AppComponent &#123;
    title = 'hello Grit';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个类实际上就是该组件的控制器，我们的业务逻辑就是在这个类中编写</p>
<ul>
<li><code>AppComponent </code>本来就是一个普通的typescript类，但是上面的组件元数据装饰器告诉Angular，AppComponent是一个组件，需要把一些元数据加到这个类上，Angular就会把AppComponent当组件来处理</li>
</ul>
<h5 data-id="heading-7">3.app文件中的app.module.ts：</h5>
<p>该文件表示模块</p>
<pre><code class="copyable">import &#123; NgModule &#125; from '@angular/core';
import &#123; BrowserModule &#125; from '@angular/platform-browser';

import &#123; AppRoutingModule &#125; from './app-routing.module';
import &#123; AppComponent &#125; from './app.component';
import &#123; ScrollableTabComponent,ImageSliderComponent &#125; from './components';
@NgModule(&#123;
  declarations: [
    AppComponent,
    ScrollableTabComponent,
    ImageSliderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
&#125;)
export class AppModule &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Angular 应用是模块化的，它拥有自己的模块化系统，称作 NgModule。每个 Angular 应用都至少有一个 NgModule 类，也就是根模块，在app.module.ts文件中，这个根模块就可以启动你的应用。</p>
<ul>
<li>
<p><code>declarations</code>（可声明对象表） —— 那些属于本 NgModule 的组件、指令、管道。</p>
</li>
<li>
<p><code>exports</code>（导出表） —— 那些能在其它模块的<em>组件模板</em>中使用的可声明对象的子集。</p>
</li>
<li>
<p><code>imports</code>（导入表） —— 导入其他模块</p>
</li>
<li>
<p><code>providers</code> —— 依赖注入</p>
</li>
<li>
<p><code>bootstrap</code> —— 设置根组件</p>
</li>
</ul>
<h4 data-id="heading-8">五、项目创建、运行</h4>
<pre><code class="copyable">ng new myProject  //项目默认会新建一个目录（项目工程）
cd myProject 
ng serve  //会启动开发环境下的Http 服务器

<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考文献：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fangular.cn%2Fapi%2Fcore%2FViewChild" target="_blank" rel="nofollow noopener noreferrer" title="https://angular.cn/api/core/ViewChild" ref="nofollow noopener noreferrer">Angular官网</a></p></div>  
</div>
            