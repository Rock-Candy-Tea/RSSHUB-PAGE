
---
title: 'Electron+Vue3 MAC 版日历开发记录(9)——Vuex 使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 05:51:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第9天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此，几个核心的主要功能有了，开始围绕功能的周边着手开发。</p>
<p>首当其冲的是：「设置功能」。要完成设置功能，核心的是配置数据的「缓存」，只有把数据缓存下来，设置才有其价值，而作为一个客户端，数据存储在本地，也就理所应当了，在这里我主要使用的是：<a href="https://www.npmjs.com/package/vuex-persistedstate" target="_blank" rel="nofollow noopener noreferrer">vuex-persistedstate</a>。</p>
<p>之前开发的功能，都有其需要配置的东西，我统一放在一个页面上，具体如下展示 (请忽略界面，确实难看！)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99977f23835c4d71883f186a6b8fd2a0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面就拿专注时间作为案例说明如何使用 <code>vuex</code> 开发设置功能的。</p>
<h2 data-id="heading-0">Vuex Store 类</h2>
<p>其实很多地方，包括 Vue 官网也提供了关于 Vuex 的<a href="https://next.vuex.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">开发指导文档</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53178843038d475bb6edb9e9c02ff5a6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>核心的主要包括：<code>State</code>、<code>Getters</code>、<code>Mutations</code>、<code>Actions</code> 等几个概念。
创建代码和官网说的没什么差别：</p>
<pre><code class="copyable">export const store = createStore<State>(&#123;
  state: &#123;
    showFestivals: false,
    showWeather: false,
    location: &#123;
      longitude: 114.52,
      latitude: 38.02,
    &#125;,
    focusTime: 40,
  &#125;,
  mutations: &#123;
    changeShowFestivals(state) &#123;
      state.showFestivals = !state.showFestivals;
    &#125;,
    changeShowWeather(state) &#123;
      state.showWeather = !state.showWeather;
    &#125;,
    changeLocation(state, location) &#123;
      state.location = &#123;
        longitude: location.longitude,
        latitude: location.latitude,
      &#125;;
    &#125;,
    changeFocusTime(state, focusTime) &#123;
      state.focusTime = focusTime;
    &#125;,
  &#125;,
  actions: &#123;
    changeShowFestivals(&#123; commit &#125;) &#123;
      commit('changeShowFestivals');
    &#125;,
    changeShowWeather(&#123; commit &#125;) &#123;
      commit('changeShowWeather');
    &#125;,
    changeLocation(&#123; commit &#125;) &#123;
      commit('changeLocation');
    &#125;,
  &#125;,
  plugins: [dataState],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 <code>State</code> 主要包含：</p>
<pre><code class="copyable">export interface State &#123;
  showFestivals: boolean,
  showWeather: boolean,
  location: &#123;
    longitude: number, // 经度
    latitude: number,  // 纬度
  &#125;,
  focusTime: number, // 专注时间
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于想到一个核心诉求是，如何同时把这些状态数据也保存到本地中，所以使用了一个第三方插件：
<a href="https://www.npmjs.com/package/vuex-persistedstate" target="_blank" rel="nofollow noopener noreferrer">vuex-persistedstate</a></p>
<blockquote>
<p>Persist and rehydrate your Vuex state between page reloads.</p>
</blockquote>
<pre><code class="copyable">const dataState = createPersistedState(&#123;
  paths: ['data'],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体完整代码看 <a href="https://github.com/fanly/fanlymenu/blob/main/packages/renderer/src/store/index.ts" target="_blank" rel="nofollow noopener noreferrer">Github 代码库</a></p>
<p>有了 <code>Store</code> 功能，接下来就开始使用了。</p>
<h2 data-id="heading-1">增加时间选择器</h2>
<p>在上文<a href="https://juejin.cn/post/6971358611012337695" target="_blank">Electron+Vue3 MAC 版日历开发记录(8)——专注模式</a>的设置中，增加一个时间选择器：</p>
<pre><code class="copyable"><div class="p-p-4" style="text-align:center;">
  <Knob
    v-model="focus_time"
    :step="5"
    :min="5"
    :max="120"
  />
  <Button
    type="button"
    :label="focusLabel"
    icon="pi pi-play"
    class="p-d-block p-mx-auto p-button-success"
    @click="focus"
  />
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里选择时间在 5 分-120 分之间，<code>focus_time</code>就是我们需要缓存下来的，以便下次使用时，不需要再去调整专注时间了。</p>
<p>使用 <code>Store</code>:</p>
<pre><code class="copyable">// SettingSub.vue
import &#123; useStore &#125; from '/@/store';

setup() &#123;
const store = useStore();
return &#123;
  store,
&#125;;
&#125;,

mounted() &#123;
    this.focus_time = this.store.state.focusTime;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里直接通过 <code>state</code> 获取 <code>focusTime</code>。</p>
<p>随着选择新的值，按 <code>Button</code> 执行 <code>click</code>：</p>
<pre><code class="copyable">  <Button
    type="button"
    :label="focusLabel"
    icon="pi pi-play"
    class="p-d-block p-mx-auto p-button-success"
    @click="focus"
  />
  
focus(): void &#123;
  this.store.commit('changeFocusTime', this.focus_time);
  this.$emit('focusClick');
  this.$emit('update:visibleFullSetting', this.sidebarVisible = false);
  window.electron.ipcRenderer.send('show-focus-window');
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用 <code>this.store.commit</code> 执行 <code>mutations</code> 的 <code>changeFocusTime</code> 方法。</p>
<p>至此，数据就缓存下来了，启动「专注」界面，在上文<a href="https://juejin.cn/post/6971358611012337695" target="_blank">Electron+Vue3 MAC 版日历开发记录(8)——专注模式</a> 的基础上，我们把 <code>focus_time</code> 给 <code>deadline</code>。</p>
<pre><code class="copyable">provide() &#123;
return &#123;
  deadline: computed(() => Moment().add(this.store.state.focusTime, 'minute').format()),
&#125;;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里利用 Vue 官网介绍的 <code>Provide / Inject</code> 中说的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b704642f167440098349d219ae1b5a1f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>至于 <code>Provide / Inject</code> 的使用放在后面的理论篇好好介绍。</p>
</blockquote>
<h2 data-id="heading-2">小结</h2>
<p>为了结合 <code>Vuex</code> 和 <code>Provide / Inject</code> 使用，看了不少官方文档说明和各个教程。完全可以写成一篇新记录出来 (其中，其他的设置状态就不再重复记录了)。</p>
<p>下一步，我们将完善已有功能的同时，开发新功能：「事件和任务」功能，具体如：亲朋好友的生日记录下来，到时候友情提醒。</p>
<p>未完待续！</p>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：
<a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a></p></div>  
</div>
            