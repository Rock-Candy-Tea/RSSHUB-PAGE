
---
title: 'Electron+Vue3 MAC 版日历开发记录(22)——配置 Tray 显示功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 05:50:01 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第22天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天想要实现的功能，主要想法来自于以下几个截图，对我们菜单栏(Tray)的日期显示做配置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8a8610693594b11852105be2f47d9c1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c379d1c7d832456cadd39013f614a583~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3c17a41bb046dbbfa84522a99136af~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/beaca99c90a84505bd3d798ca10fdc25~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed4f8041e8be46ea8d7e064537fc8687~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5d3cc3e9e90446ca9f71306b1bbf259~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但我们一开始没想着这么复杂 (随着项目的推荐，会不断完善)，只想对 Tray 做一个合理的使用，本身菜单栏能显示的区域不大，如果占据了太多，对其他应用的显示也不友好：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075a0d79ece44bbe98f6ef111e781429~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于每个人都有不同的显示数据的需要，所以完全有必要做一个 Setting 来配置 Tray 时间的显示。</p>
<h2 data-id="heading-0">增加 Setting 页面</h2>
<p>增加一个 Setting 页面用于配置 Tray 显示的参数配置，再加上之前的 Setting，配置项增加了不少，所以在 Setting 组件里，我该用了 Naive UI 的 <a href="https://www.naiveui.com/zh-CN/os-theme/components/tabs" target="_blank" rel="nofollow noopener noreferrer"><code>NTabs</code></a> 标签页组件来切换不同的配置项。</p>
<p>先看看效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24f816c940ff40e7b6b51603799add50~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体代码主要参考官网文档来的，也比较简单：</p>
<pre><code class="copyable"><template>
  <n-drawer-content
    title="设置"
    closable
  >
    <n-tabs
      default-value="normalSetting"
      size="large"
    >
      <n-tab-pane
        name="normalSetting"
        tab="通用设置"
      >
        <n-space vertical>
          <h4>获取节假日</h4>
          <n-switch
            v-model:value="inputSwitchFestivalsModel"
            size="large"
            @update-value="updateFestivalsModel"
          />
          <h4>获取天气预报</h4>
          <n-switch
            v-model:value="inputSwitchWeatherModel"
            size="large"
            @update-value="updateWeatherModel"
          />
          <n-space
            v-if="inputSwitchWeatherModel"
            inline
          >
            <n-input-number
              v-model:value="longitude"
              :min="-180"
              :max="180"
              :show-button="false"
              placeholder="经度"
              @update:value="changeLocalLocation"
            />
            <n-input-number
              v-model:value="latitude"
              :min="-90"
              :max="90"
              :show-button="false"
              placeholder="纬度"
              @update:value="changeLocalLocation"
            />
          </n-space>
        </n-space>
      </n-tab-pane>
      <n-tab-pane
        name="menuSetting"
        tab="菜单栏设置"
      >
        <n-space vertical>
          <h4>显示节假日(农历)</h4>
          <n-switch
            v-model:value="trayFestivalsModel"
            size="large"
            @update-value="updateTraySetting"
          />
          <h4>显示天气预报</h4>
          <n-switch
            v-model:value="trayWeatherModel"
            size="large"
            @update-value="updateTraySetting"
          />
          <h4>显示星期</h4>
          <n-switch
            v-model:value="trayWeekModel"
            size="large"
            @update-value="updateTraySetting"
          />
          <h4>显示秒钟</h4>
          <n-switch
            v-model:value="traySecondsModel"
            size="large"
            @update-value="updateTraySetting"
          />
        </n-space>
      </n-tab-pane>
      <n-tab-pane
        name="focusSetting"
        tab="专注设置"
      >
        <n-space vertical>
          <n-slider
            v-model:value="focus_time"
            :step="5"
            :min="5"
            :max="120"
          />
          <n-button
            type="primary"
            size="large"
            @click="focus"
          >
            <template #icon>
              <n-icon>
                <caret-right-icon />
              </n-icon>
            </template>
            &#123;&#123; focusLabel &#125;&#125;
          </n-button>
        </n-space>
      </n-tab-pane>
    </n-tabs>
  </n-drawer-content>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要菜单栏的参数有变化，我们就直接用 <code>electron.ipcRenderer.send</code> 把参数推送到 Main 主线程去获取：</p>
<pre><code class="copyable">updateTraySetting(): void &#123;
  window.electron.ipcRenderer.send('updateTraySetting', &#123;
    trayFestivalsModel: this.trayFestivalsModel,
    trayWeatherModel: this.trayWeatherModel,
    trayWeekModel: this.trayWeekModel,
    traySecondsModel: this.traySecondsModel,
  &#125;);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">配置 Tray 时间显示参数</h2>
<p>每次获取变化的参数后，我们都需要对参数作处理，拼接成 Momentjs 可识别的格式，在这里我需要感谢 <a href="https://momentjs.com/" target="_blank" rel="nofollow noopener noreferrer">Momentjs</a> 插件，提供了不少 <code>format</code> 参数配置。</p>
<pre><code class="copyable">moment().format('MMMM Do YYYY, h:mm:ss a'); // June 22nd 2021, 9:11:20 pm
moment().format('dddd');                    // Tuesday
moment().format("MMM Do YY");               // Jun 22nd 21
moment().format('YYYY [escaped] YYYY');     // 2021 escaped 2021
moment().format();                          // 2021-06-22T21:11:20+08:00
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体 format 拼接方法如下：</p>
<pre><code class="copyable">// ClockService.js
  /* &#123;
    trayFestivalsModel: true,
    trayWeatherModel: false,
    trayWeekModel: true,
    traySecondsModel: true
  &#125;*/
  setParams(params: any) &#123;
    this.params = params;

    // MMMDo dddd HH:mm:ss
    let default_format = 'MMMDo ';

    if (this.params.trayWeekModel) &#123;
      default_format = default_format.concat('dddd ');
    &#125;

    default_format = default_format.concat('HH:mm');

    if (this.params.traySecondsModel) &#123;
      default_format = default_format.concat(':ss');
    &#125;

    return this.setFormat(default_format);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个参数是：是否显示农历：</p>
<pre><code class="copyable">// ClockService.js
  toString(): string &#123;
    let showString = '';
    if (this.params.trayFestivalsModel) &#123;
      const lunarService = new LunarService();
      const dayTextInChinese = lunarService.showNongliData(true);
      showString = showString.concat(...[dayTextInChinese, ' ']);
    &#125;

    return showString.concat(Moment().format(this.getFormat()));
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，基本就能达到在 Setting 配置后，可以实时看到 Tray 显示的变化。</p>
<p>当然，在获取事件那，增加一个捕获方法：</p>
<pre><code class="copyable">ipcMain.on('updateTraySetting', (_, params) => &#123;
  if (mainApp == null) &#123;
    mainApp = new App();
  &#125;
  mainApp.setClockParams(params);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体运行效果可以 <a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">fork 代码</a>实际看看～～</p>
<h2 data-id="heading-2">继续重构部分</h2>
<p>今天继续昨天说的那个问题，怎么把多个 <code>n-drawer</code>合并成为一个：</p>
<pre><code class="copyable"><n-drawer
    v-model:show="visibleFullSetting"
    :width="settingDrawerWidth"
    placement="left"
  >
    <setting-sub
      v-model:changeShowWeather="changeShowWeather"
      v-model:changeShowFestivals="changeShowFestivals"
      v-model:location="location"
      @focusClick="focusClick"
    />
  </n-drawer>
  <n-drawer
    v-model:show="visibleFullDateView"
    :width="hlDrawerWidth"
    placement="left"
  >
    <date-view-sub
      v-model:date="date"
    />
  </n-drawer>
  <n-drawer
    v-model:show="visibleECSub"
    :width="ecDrawerWidth"
    placement="left"
  >
    <event-create-sub
      v-model:event="event"
      @addEventClick="addEventClick"
    />
  </n-drawer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要用到了 Vue 官网文档说的一个概念：<a href="https://v3.cn.vuejs.org/guide/computed.html" target="_blank" rel="nofollow noopener noreferrer">计算属性和侦听器</a></p>
<blockquote>
<p>Vue 提供了一种更通用的方式来观察和响应当前活动的实例上的数据变动：侦听属性。当你有一些数据需要随着其它数据变动而变动时，你很容易滥用 watch——特别是如果你之前使用过 AngularJS。然而，通常更好的做法是使用计算属性而不是命令式的 watch 回调。细想一下这么重构之后：</p>
</blockquote>
<pre><code class="copyable"><n-drawer
    v-model:show="showDrawer"
    :width="settingDrawerWidth"
    placement="left"
  >
    <setting-sub
      v-if="visibleFullSetting"
      v-model:changeShowWeather="changeShowWeather"
      v-model:changeShowFestivals="changeShowFestivals"
      v-model:location="location"
      @focusClick="focusClick"
    />
    <date-view-sub
      v-if="visibleFullDateView"
      v-model:date="date"
    />
    <event-create-sub
      v-if="visibleECSub"
      v-model:event="event"
      @addEventClick="addEventClick"
    />
  </n-drawer>
  
  // watch
  visibleFullSetting(newValue) &#123;
  this.showDrawer = newValue || this.visibleFullDateView || this.visibleECSub;
&#125;,
visibleFullDateView(newValue) &#123;
  this.showDrawer = this.visibleFullSetting || newValue || this.visibleECSub;
&#125;,
visibleECSub(newValue) &#123;
  this.showDrawer = this.visibleFullSetting || this.visibleFullDateView || newValue;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是命令式且重复的，并且 <code>showDrawer</code> 是 Model 动态绑定的，本身修改不会改变这三个变量，所以我们进一步改进，将它与计算属性的版本进行比较：</p>
<pre><code class="copyable">  computed: &#123;
    showDrawer(): boolean &#123;
      return this.visibleFullSetting || this.visibleFullDateView || this.visibleECSub;
    &#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好很多了，不是吗？</p>
<p>但这时候会提示 <code>showDrawer</code>，是只读的，所以我们需要加入 Setter。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c16430f92dcd472892de2f9a7c15fb2f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">计算属性的 Setter</h3>
<pre><code class="copyable">// ...
  computed: &#123;
    showDrawer: &#123;
      // getter
      get(): boolean &#123;
        return this.visibleFullSetting || this.visibleFullDateView || this.visibleECSub;
      &#125;,
      // setter
      set(newValue: boolean) &#123;
        this.visibleFullSetting = newValue;
        this.visibleFullDateView = newValue;
        this.visibleECSub = newValue;
      &#125;
    &#125;,
  &#125;,
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么一顿操作后，如果直接点「关闭」<code>n-drawer</code> 按钮后，触发 <code>set</code> 方法，把这几个人变量重置为 <code>false</code>。保证代码的准确性和完整性。</p>
<h2 data-id="heading-4">小结</h2>
<p>今晚主要完成 Tray 显示的动态配置功能和已知遗留的小尾巴继续重构。</p>
<p>明天我们继续今天没完成的「天气」的 Tray 展示，明天继续。未完待续！</p>
<blockquote>
<p>代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            