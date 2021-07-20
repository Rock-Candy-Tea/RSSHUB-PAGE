
---
title: 'Electron+Vue3 MAC 版日历开发记录(32)——使用vueuse'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a7219c2b15346318b2004063ef740ae~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 06:47:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a7219c2b15346318b2004063ef740ae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天本来想着提交一版，但发现有一个功能没实现，那就是：每隔一段时间实时获取天气预报。</p>
<p>在之前的 <code>ClockService</code> 类中，我们使用到 <code>setInterval(fn, 1000)</code> 来做定时器，在当时为了一些 Typescript type 搞得焦头烂额，后来一直想着用 <code>vueuse</code>，这回有了理由了。</p>
<pre><code class="copyable">// ClockService.ts
'use strict';

import &#123; app &#125; from 'electron';
const Moment = require('moment');
import LunarService from './LunarService';

export default class ClockService &#123;
  format = 'MMMDo HH:mm';
  // onTickHandler: ((toString: (arg0: ClockService) => string) => void) | null = null;
  onTickHandler: ((arg0: ClockService) => void) | null = null;
  intervalId: NodeJS.Timeout | null = null;
  params: ClockSettingParams;
  constructor() &#123;
    Moment.locale(app.getLocale());
    this.params = &#123;&#125; as ClockSettingParams;
    // lll MMMDo dddd HH:mm:ss
    this.setFormat('MMMDo HH:mm');
    this.start();
  &#125;

  start(): this &#123;
    if (typeof this.onTickHandler !== 'function') &#123;
      this.onTickHandler = () => &#123;&#125;;
    &#125;

    this.intervalId = setInterval(() => &#123;
      if (this.onTickHandler) &#123;
        this.onTickHandler(this);
      &#125;
    &#125;, 1000);

    return this;
  &#125;

  stop(): this &#123;
    if (this.intervalId) &#123;
      clearInterval(this.intervalId);
      this.intervalId = null;
    &#125;

    return this;
  &#125;

  onTick(callback: ((arg0: ClockService) => void) | null): this &#123;
    this.onTickHandler = callback;

    return this;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">useIntervalFn</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a7219c2b15346318b2004063ef740ae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Collection of essential Vue Composition Utilities
官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/" ref="nofollow noopener noreferrer">vueuse.org/</a></p>
</blockquote>
<p>有了 <code>vueuse</code>，我们就可以直接使用 useIntervalFn <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2Fshared%2FuseIntervalFn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/shared/useIntervalFn/" ref="nofollow noopener noreferrer">vueuse.org/shared/useI…</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60d72d08c7e241308a0f46c4ea10bd5f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装 vueuse：</p>
<pre><code class="copyable">yarn add @vueuse/core
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先在 <code>setup</code> 里重写 <code>getWeather</code> 方法：</p>
<pre><code class="copyable">const getWeather = async (location: FLocation) => &#123;
  const weatherService = new WeatherService();
  weather.value = await weatherService.getWeathers(location);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>紧接着就可以使用 vueuse 提供的函数了：</p>
<pre><code class="copyable">const changeShowWeather = ref(false);

const intervalFnOptions = reactive(&#123;
  immediate: changeShowWeather.value,
&#125; as IntervalFnOptions);

const &#123; pause, resume, isActive &#125; = useIntervalFn(() => &#123;
  getWeather(store.state.location);
&#125;, 7200000, intervalFnOptions);

return &#123;
  weather,
  eventService,
  visibleFullSetting,
  store,
  event,
  getWeather,
  pause,
  resume,
  isActive,
  changeShowWeather,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就可以将对应的参数和函数 return 出去了。</p>
<p>在 watch 里，实时监听 <code>changeShowWeather</code> 值，随着设置里修改 changeShowWeather，就可以在此函数里重启或者停止该监听器：</p>
<pre><code class="copyable">  watch: &#123;
    changeShowWeather(newval) &#123;
      this.store.commit('changeShowWeather', newval);
      if (this.changeShowWeather) &#123;
        this.getWeather(this.store.state.location);
        // 增加定时器，每隔2个小时更新一次天气预报
        this.resume();
      &#125; else &#123;
        this.pause();
      &#125;
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，就可以达到每隔两小时重新请求 <code>getWeathers</code> 获取天气预报了。</p>
<p>到此，我们使用到了 <code>useIntervalFn</code>。</p>
<h2 data-id="heading-1">源码</h2>
<p>学习源码是最好提升自我能力的方法，我们把源码 copy 出来给大家看看：</p>
<pre><code class="copyable">import &#123; ref &#125; from 'vue-demi'
import &#123; tryOnUnmounted &#125; from '../tryOnUnmounted'
import &#123; Pausable, Fn, isClient &#125; from '../utils'

export interface IntervalFnOptions &#123;
  /**
   * Execute the callback immediate after calling this function
   *
   * @default true
   */
  immediate?: boolean
&#125;

/**
 * Wrapper for `setInterval` with controls
 *
 * @param cb
 * @param interval
 * @param options
 */
export function useIntervalFn(cb: Fn, interval = 1000, options: IntervalFnOptions = &#123;&#125;): Pausable &#123;
  const &#123;
    immediate = true,
  &#125; = options

  let timer: any = null
  const isActive = ref(false)

  function clean() &#123;
    if (timer) &#123;
      clearInterval(timer)
      timer = null
    &#125;
  &#125;

  function pause() &#123;
    isActive.value = false
    clean()
  &#125;

  function resume() &#123;
    if (interval <= 0)
      return
    isActive.value = true
    clean()
    timer = setInterval(cb, interval)
  &#125;

  if (immediate && isClient)
    resume()

  tryOnUnmounted(pause)

  return &#123;
    isActive,
    pause,
    resume,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们重构刚开始说的那个 <code>ClockService</code> 类：</p>
<pre><code class="copyable">import type &#123; Pausable &#125; from '@vueuse/core';

export default class ClockService &#123;
  format = 'MMMDo HH:mm';
  onTickHandler: ((arg0: ClockService) => void) | null = null;
  pausable: Pausable;
  params: ClockSettingParams;
  constructor() &#123;
    Moment.locale(app.getLocale());
    this.params = &#123;&#125; as ClockSettingParams;
    // lll MMMDo dddd HH:mm:ss
    this.setFormat('MMMDo HH:mm');
    this.pausable = useIntervalFn(() => &#123;
      if (this.onTickHandler) &#123;
        this.onTickHandler(this);
      &#125;
    &#125;, 1000);
    this.start();
  &#125;

  start(): this &#123;
    if (typeof this.onTickHandler !== 'function') &#123;
      this.onTickHandler = () => &#123;&#125;;
    &#125;

    this.pausable.resume();

    return this;
  &#125;

  stop(): this &#123;
    this.pausable.pause();

    return this;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就很简单，直接看代码，不用再做解释了。</p>
<h2 data-id="heading-2">总结</h2>
<p>我们完全可以直接参考 vueuse 提供的源代码，不需要引用这个插件，但我们发现还有很多地方可以用到，比如 @vueuse/electron 相关的功能 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2Felectron%2FREADME.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/electron/README.html" ref="nofollow noopener noreferrer">vueuse.org/electron/RE…</a>，也可以在这个过程中，好好学习我心中的大神是如何封装函数和做开源代码的。</p></div>  
</div>
            