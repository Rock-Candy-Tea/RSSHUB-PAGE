
---
title: 'Electron+Vue3 MAC 版日历 开发记录(2)——功能清单'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 15:37:13 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">目前状态</h2>
<p><a href="https://juejin.cn/post/6968670953836380196" target="_blank">第一天的记录</a>基本交代了制作 Mac 版日历的初衷，在上干货之前，还是总结下到目前为止已经完成的部分功能清单 (使用 Things 3 记录)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef2334030a144564bc551c0a997f0b44~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>和未来要做的功能列表 (都是在看到或者想到的实时记录下来，便于下一步开发)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac034b2c57f24286aa94478e24cbe969~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了督促自己每天都需要写写代码，所以我直接以 generated from cawa-93/vite-electron-builder，在 Github 创建自己长时间维护的这个项目：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">fanly/fanlymenu</a>。</p>
<blockquote>
<p>欢迎大家 fork，或者提出更多建议和产品功能清单。</p>
</blockquote>
<blockquote>
<p>同时，也说一个题外话，把代码开源了，就好比参加这次<a href="https://juejin.cn/post/6967194882926444557" target="_blank">活动</a>，都是希望有人帮忙监督，让自己不断完善。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3d50ed8235e47c39197f3575631482d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">功能清单</h2>
<p>从上文也能看出来，我想实现的核心功能主要有：</p>
<ol>
<li>显示农历；</li>
<li>根据需要，显示节假日名称；</li>
<li>显示黄历；</li>
<li>显示天气预报；</li>
<li>增加事件功能，也就是 GTD 相关功能；</li>
<li>增加和时间轴有关的消息展示功能 (如家人、亲朋好友、同事的生日等)；</li>
<li>同步自带日历、Google 日历事件功能；</li>
<li>todo (还有很多，有待于下一步更新)。</li>
</ol>
<h2 data-id="heading-2">代码目标</h2>
<p>使用 Electron + Vue3 + TypeScript，核心还是学习其开发原理，掌握各个框架和语言思维。</p>
<h3 data-id="heading-3">Electron</h3>
<p>无论是现在很火的代码 IDE：VS Code，还是 InVision，都使用 <a href="https://www.electronjs.org/" target="_blank" rel="nofollow noopener noreferrer">Electron</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1890cf338e1d4ca7a7a4bc7849d094e8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而在这里，我想了解如何通过「消息事件」从 Main 进程将消息传递给渲染器进程，以及如何借助 <code>Preload scripts</code> 达到目标，如本文代码：</p>
<pre><code class="copyable">createWindow(): BrowserWindow &#123;
const window = new BrowserWindow(&#123;
  width: 600,
  height: 700,
  resizable: false,
  alwaysOnTop: true,
  show: false,
  frame: false,
  webPreferences: &#123;
    webSecurity: false,
    preload: join(__dirname, '../../preload/dist/index.cjs'),
    contextIsolation: this.env.MODE !== 'test',   // Spectron tests can't work with contextIsolation: true
    enableRemoteModule: this.env.MODE === 'test', // Spectron tests can't work with enableRemoteModule: false
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <code>preload/src/index.ts</code>，增加 <code>ipcRenderer</code>：</p>
<pre><code class="copyable">import &#123;contextBridge, ipcRenderer&#125; from 'electron';

const apiKey = 'electron';
/**
 * @see https://github.com/electron/electron/issues/21437#issuecomment-573522360
 */
const api: ElectronApi = &#123;
  versions: process.versions,
  ipcRenderer: ipcRenderer,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以在 Renderer 层的 Vue 代码中直接调用：</p>
<pre><code class="copyable">quit(): void &#123;
    window.electron.ipcRenderer.send('quit');
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给 Main 层发送 <code>quit</code> 退出 APP 的消息事件，最后在 Main 层捕获，并执行相对于的操作：</p>
<pre><code class="copyable">import &#123; app, protocol, ipcMain &#125; from 'electron';

...

ipcMain.on('quit', () => &#123;
  app.quit();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：具体代码分析，看后续的记录！</p>
</blockquote>
<h3 data-id="heading-4">Vue 3</h3>
<p>正如尤雨溪作者说的，推荐大家直接使用 Vue 3，有很多地方值得推敲和学习，比如，在模板代码中使用多个 Model，以及 Model 有层级关系，这时候用 Vue 3 就显得很方便：</p>
<pre><code class="copyable"><template>
  <div>
    <fullcalendar-sub
      v-model:changeShowFestivals="changeShowFestivals"
      v-model:changeShowWeather="changeShowWeather"
      v-model:weather="weather"
      v-model:location="location"
      @settingClick="visibleFullSetting = true"
      @dateClick="dateClick"
    />
    <weather-sub
      v-if="changeShowWeather"
      v-model:changeShowWeather="changeShowWeather"
      v-model:weather="weather"
      v-model:location="location"
    />
    <setting-sub
      v-model:visibleFullSetting="visibleFullSetting"
      v-model:changeShowWeather="changeShowWeather"
      v-model:changeShowFestivals="changeShowFestivals"
      v-model:location="location"
    />
    <date-view-sub
      v-model:visibleFullDateView="visibleFullDateView"
      v-model:date="date"
    />
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而这里，还有一些祖孙传递关系，可以直接使用函数处理同步回传：</p>
<pre><code class="copyable"><InputSwitch
  v-model="inputSwitchWeatherModel"
  @change="$emit('update:changeShowWeather', inputSwitchWeatherModel)"
/>

...

emits: [
'update:visibleFullSetting',
'update:changeShowFestivals',
'update:changeShowWeather',
'update:location',
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体使用，<a href="https://v3.cn.vuejs.org/guide/component-custom-events.html#%E5%A4%9A%E4%B8%AA-v-model-%E7%BB%91%E5%AE%9A" target="_blank" rel="nofollow noopener noreferrer">参考官网文档</a></p>
<h3 data-id="heading-5">TypeScript</h3>
<p>在 <code>vite-electron-builder</code> 模板中，还是 Javascript 占的比例多，所以接下来如何使用 TypeScript，并提高 TypeScript 占比是我的下一步目标：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/620a62b7b38b42d1ac27c970105f3b15~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，自己也买了相关的书，作为工具书，放在旁边，可以随时翻看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3395a9b738dc4d39809b1415231061f3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">小结</h2>
<p>今天主要整理出目前的功能完成情况，主要功能清单，以及在这过程，我想学到的关于 Electron、Vue 3 和 TypeScript 知识。</p>
<p>明天开始进入功能总结的干货记录阶段，未完待续。</p></div>  
</div>
            