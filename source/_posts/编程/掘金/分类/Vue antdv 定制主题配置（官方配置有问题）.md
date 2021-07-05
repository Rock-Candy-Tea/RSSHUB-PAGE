
---
title: 'Vue antdv 定制主题配置（官方配置有问题）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3826008c4494114b938b566614e0e3c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 01:03:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3826008c4494114b938b566614e0e3c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一、简介</h4>
<ul>
<li>在使用 <code>ant-design-vue</code> 时，需要修改一下全局的主题颜色，按照官方的配置流程配置失败，应该是版本问题。</li>
</ul>
<h4 data-id="heading-1">二、安装 <code>antdv</code></h4>
<ul>
<li>
<p>安装 <code>ant-design-vue</code></p>
<pre><code class="copyable">$ npm i --save ant-design-vue
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>main.js</code> 中配置，完整引入</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// 引入 antdv
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

Vue.config.productionTip = false

// 注册 antdv
Vue.use(Antd);

new Vue(&#123;
  router,
  store,
  render: h => h(App)
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用按钮，这是默认样式</p>
<pre><code class="copyable"><template>
  <!-- 使用按钮 -->
  <a-button type="primary">Primary</a-button>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3826008c4494114b938b566614e0e3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h4 data-id="heading-2">三、自定义主题样式</h4>
<ul>
<li>
<p><code>antdv</code> 的样式使用了 <code>Less</code> 作为开发语言，所以需要安装 <code>Less</code> 环境。</p>
</li>
<li>
<p><a href="https://www.antdv.com/docs/vue/customize-theme-cn/" target="_blank" rel="nofollow noopener noreferrer">参考 - 官方自定义主题文档</a></p>
</li>
<li>
<p><a href="https://github.com/vueComponent/ant-design-vue/blob/master/components/style/themes/default.less" target="_blank" rel="nofollow noopener noreferrer">参考 - 所有样式变量</a></p>
</li>
<li>
<p>参考 - 以下是一些最常用的通用变量</p>
<pre><code class="copyable">@primary-color: #1890ff; // 全局主色
@link-color: #1890ff; // 链接色
@success-color: #52c41a; // 成功色
@warning-color: #faad14; // 警告色
@error-color: #f5222d; // 错误色
@font-size-base: 14px; // 主字号
@heading-color: rgba(0, 0, 0, 0.85); // 标题色
@text-color: rgba(0, 0, 0, 0.65); // 主文本色
@text-color-secondary: rgba(0, 0, 0, 0.45); // 次文本色
@disabled-color: rgba(0, 0, 0, 0.25); // 失效色
@border-radius-base: 4px; // 组件/浮层圆角
@border-color-base: #d9d9d9; // 边框色
@box-shadow-base: 0 2px 8px rgba(0, 0, 0, 0.15); // 浮层阴影
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建 <a href="https://blog.csdn.net/zz00008888/article/details/109536466" target="_blank" rel="nofollow noopener noreferrer">vue.config.js</a>，加入下面配置（官方自带的这段配置是老版的，配置会无法生效）</p>
<pre><code class="copyable">module.exports = &#123;
  css: &#123;
    loaderOptions: &#123;
      less: &#123;
        // If you are using less-loader@5 please spread the lessOptions to options directly
        modifyVars: &#123;
          // 这里就是样式变量的名称以及对应的值，可以按照上面提供的官方文档进行配置
          'primary-color': '#41B883',
          'link-color': '#41B883',
          'border-radius-base': '2px'
        &#125;,
        javascriptEnabled: true
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>重新运行项目，查看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eff34f7ba1b456190f60064ee35c130~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>如果报错 <a href="https://blog.csdn.net/zz00008888/article/details/118493995" target="_blank" rel="nofollow noopener noreferrer">.bezierEasingMixin();</a>，点击看解决方案。</p>
</li>
</ul></div>  
</div>
            