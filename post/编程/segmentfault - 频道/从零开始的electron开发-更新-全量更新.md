
---
title: '从零开始的electron开发-更新-全量更新'
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-22 08:20:42
thumbnail: ''
---

<div>   
<h1>更新-全量更新</h1><h2>更新</h2><p>electron的更新一般来说有两种方式，全量和增量，顾名思义全量就是下载我们打包好的exe文件或者zip文件，进行全面替换。我们之前说过electron就是用浏览器打开我们的页面，很多时候我们的更新可能只会修改渲染进程，那么我们把我们的渲染进程的文件给替换了不久更新吗，也就是说增量实际上是替换打包好的html，js等文件。那么更新的方式如下：</p><ul><li>主进程修改：全量更新</li><li>渲染进程修改：全量或增量更新</li></ul><p>增量更新放到下一期来说，本篇是讲全量更新的事，本文旨在对全量更新进行详细的说明，包括主进程的更新流程和渲染进程展示等以及更新问题如何排查。</p><h2>更新流程</h2><p>我们这里先说明一下我们的处理流程：</p><ul><li>我们的渲染进程请求接口，接口返回了更新信息，拿到更新信息进行版本对比以及更新逻辑判断。</li><li>渲染进程全量更新通过，把信息传递给主进程</li><li>主进程拿到信息实现更新，把更新信息推送给渲染进程</li><li>渲染进程进行更新状态以及进度的显示，完成更新</li></ul><h2>electron-updater</h2><p>全量更新我们使用的是<code>electron-updater</code>这个包，进入我们的项目：</p><pre><code>npm i -D electron-updater</code></pre><p>electron-updater更新只需要把一个url传入，然后它会自动查找<code>$&#123;url&#125;/xxx.yml</code>文件，根据这个<code>yml</code>文件检测更新及下载，我们可以通过其各种事件拿到对应的更新状态，下载完成之后调用<code>autoUpdater.quitAndInstall()</code>重启当前的应用并且安装更新  <br>这个url下是放静态资源的，简单来说就是这个链接类似访问一个目录，这个目录下需要有更新的文件以及检测更新的文件。  <br>需要哪些东西呢：</p><ul><li>win: latest.yml，exe文件</li><li>mac：latest-mac.yml，zip文件</li></ul><p>总的来说我们就是要一个url实现更新，先让渲染进程把这个url传过来吧，我们先模拟一下更新请求。</p><h2>更新请求</h2><h3>模拟更新请求</h3><p>一般来说，更新都是调用后端接口，上面说了更新需要一个url，那么我们这里就用json文件模拟请求以及模拟更新文件的地址</p><pre><code>npm i -g  http-server
新建一个目录server
http-server ./ -p 4000   // 启一个4000端口的服务http://127.0.0.1:4000
server下新建一个index.json来当接口返回数据
&#123;
  "code": 200,
  "success": true,
  "data": &#123;
    "forceUpdate": false, // 是否强制更新
    "fullUpdate": true, // 是否全量更新
    "upDateUrl": "http://127.0.0.1:4000/", // electron-updater传入的url
    "restart": true,  // 增量更新是否重启
    "message": "我要升级成0.0.2", // 更新说明
    "version": "0.0.2" // 版本号
  &#125;
&#125;
浏览器打开http://localhost:4000/，看是否有index.json。

我们在渲染进程用请求获取index.json的数据（这里是我自己做的api请求封装）
const api = proxy.$api
api('http://localhost:4000/index.json', &#123;&#125;, &#123; method: 'get' &#125;).then(res => &#123;
  console.log(res)
&#125;)</code></pre><h3>打高版本包</h3><p>然后我们打一个高版本包，这里是打dev包，修改<code>.env.dev</code>的<code>VUE_APP_VERSION</code>为0.0.2</p><pre><code>npm run build:dev:win64
mac同理，将打包好的文件放入server目录
win：latest.yml，0.0.2的exe
mac：latest-mac.yml，0.0.2的zip（注意是zip不是dmg）</code></pre><h3>跨域处理</h3><p>不出意料的话会报一个跨域的错误，毕竟我们的端口号不同，在electron中我们的权限要比浏览器中大得多，<br>我们可以把同源策略关闭，就不会出现跨域的问题了，可以得到返回了。</p><pre><code>BrowserWindow的
webPreferences: &#123;
  .....
  webSecurity: false
&#125;</code></pre><p>补充：当然还有其他跨域的处理方式，想了解的话可以看一下我对跨域的说明<a href="https://xuxin123.com/%e8%b7%a8%e5%9f%9f%e4%b8%8enginx%e4%bb%a3%e7%90%86/" rel="nofollow">链接</a></p><h2>渲染进程检测更新</h2><h3>检测更新</h3><p>当前我们的版本号的话，是在<code>.env</code>里面设置的，不知道的可看搭建篇环境变量说明。开发时不用检测版本更新，所以有个判断。<br>isClick是自动检测的话没有message提示，手动有。</p><pre><code><template>
  <div class="update">
    <div class="version">当前版本为：&#123;&#123; config.VUE_APP_VERSION &#125;&#125;</div>
    <a-button type="primary" @click="upDateClick(true)">检测更新</a-button>
  </div>
</template>

<script>
import cfg from '@/config'
import update from '@/utils/update'
import &#123; defineComponent, getCurrentInstance &#125; from 'vue'

export default defineComponent(&#123;
  setup() &#123;
    const state = reactive(&#123;
      visible: false,
      upDateData: &#123;&#125;,
      upDateProgress: &#123;
        show: false,
        percent: 0
      &#125;
    &#125;)
    const &#123; proxy &#125; = getCurrentInstance()
    const config = cfg
    const api = proxy.$api
     function upDateClick(isClick) &#123;
      api('http://localhost:4000/index.json', &#123;&#125;, &#123; method: 'get' &#125;).then(res => &#123;
        console.log(res)
        if (cfg.NODE_ENV !== 'development') &#123;
          update(config.VUE_APP_VERSION, res).then(() => &#123;
            state.upDateData = res
            if (res.fullUpdate) &#123;
              updateNotice(isClick)
            &#125; else &#123;
              console.log()
            &#125;
          &#125;).catch(err => &#123;
            if (err.code === 0) &#123;
              isClick && message.success('已为最新版本')
            &#125;
          &#125;)
        &#125; else &#123;
          message.success('请在打包环境下更新')
        &#125;
      &#125;)
    &#125;
    return &#123;
      config,
      upDateClick
    &#125;
  &#125;
&#125;)
</script></code></pre><h3>版本对比</h3><p>这里用当前版本与接口版本进行对比，向主进程发送通知（更新message弹窗）。</p><pre><code>/utils/update.js

export default (version, data) => &#123;
  return new Promise((resolve, reject) => &#123;
    const isUpdate = data ? versionCompare(data.version, version) : 0
    switch (isUpdate) &#123;
      case 0:
        console.log('不更新')
        reject(&#123; code: isUpdate &#125;)
        break;
      case 1:
        if (data.fullUpdate) &#123;
          console.log('全量更新')
          resolve()
        &#125; else &#123;
          console.log('增量更新')
        &#125;
        break
      case -1:
        console.log('降级')
        reject(&#123; code: isUpdate &#125;)
        break
    &#125;
  &#125;)
&#125;


// 1为当前版本比更新版本低，0为版本一致，-1为当前版本比更新版本高
function versionCompare(stra, strb) &#123;
  const straArr = stra.split('.')
  const strbArr = strb.split('.')
  const maxLen = Math.max(straArr.length, strbArr.length)
  let result
  let sa
  let sb
  for (let i = 0; i < maxLen; i++) &#123;
    sa = ~~straArr[i]
    sb = ~~strbArr[i]
    if (sa > sb) &#123;
      result = 1
    &#125; else if (sa < sb) &#123;
      result = -1
    &#125; else &#123;
      result = 0
    &#125;
    if (result !== 0) &#123;
      return result
    &#125;
  &#125;
  return result
&#125;</code></pre><h3>更新弹窗</h3><p>检测到更新后我们显示更新弹窗，根据<code>forceUpdate</code>判断如果是强制更新的话我们把弹窗的关闭除去，只能点确定。如果不是的话，那么点击取消后，我们记录一个更新版本号的<code>localStorage</code>，下次再检测更新时如果有值的话，更新弹窗将不会出现</p><pre><code><a-modal
  v-model:visible="visible"
  title="更新"
  @ok="upDateOk"
  @cancel="upDateCancel"
  :closable="!upDateData.forceUpdate"
  :maskClosable="false"
  :keyboard="!upDateData.forceUpdate"
  :destroyOnClose="true"
>
  <p v-html="upDateData.message"></p>
  <template #footer v-if="upDateData.forceUpdate">
    <div class="footer">
      <a-button type="primary" @click="upDateOk">确定</a-button>
    </div>
  </template>
</a-modal>

调用updateNotice(isClick)，这里是按钮点击检测更新，当然你也可以程序自动检测更新，放在App.vue中主动调用updateNotice(false)

function updateNotice(isClick) &#123;
  if (LgetItem(UPDATE_LIST) && LgetItem(UPDATE_LIST)[state.upDateData.version] && !isClick) &#123; // 用户手动点击检测的话出现弹窗
    return
  &#125;
  state.visible = true
&#125;
function upDateOk() &#123;
  state.visible = false
  window.ipcRenderer.invoke('win-update', &#123;...state.upDateData&#125;)
&#125;
function upDateCancel() &#123;
  if (!LgetItem(UPDATE_LIST)) &#123;
    LsetItem(UPDATE_LIST, &#123;&#125;)
  &#125;
  LsetItem(UPDATE_LIST, &#123; ...LgetItem(UPDATE_LIST), [state.upDateData.version]: true &#125;)
&#125;</code></pre><h2>主进程处理更新</h2><p>我们向主进程推送了更新信息<code>win-update</code></p><pre><code>ipcMain.js接收渲染进程的更新信息

import checkUpdate from './checkUpdate'

ipcMain.handle('win-update', (_, data) => &#123;
  checkUpdate(data)
&#125;)</code></pre><p>上面说了electron-updater需要一个url，我们这里实现一下其更新逻辑，<code>electron-updater</code>有各种更新状态，我们把这些状态推送<code>renderer-updateMsg</code>给渲染进程，让其有对应的提示或者进度，<code>autoUpdater.quitAndInstall()</code>被调用后会自动安装重启。</p><pre><code>新建checkUpdate.js
import &#123; autoUpdater &#125; from 'electron-updater'
import log from '../config/log.js'
import global from '../config/global'
autoUpdater.logger = log
/**
 * -1 检查更新失败 0 正在检查更新 1 检测到新版本，准备下载 2 未检测到新版本 3 下载中 4 下载完成
 **/
function Message(type, data) &#123;
  const sendData = &#123;
    type,
    data
  &#125;
  global.sharedObject.win.webContents.send('renderer-updateMsg', sendData)
&#125;

// 当更新发生错误的时候触发。
autoUpdater.on('error', (err) => &#123;
  log.info('更新出现错误')
  log.info(err.message)
  if (err.message.includes('sha512 checksum mismatch')) &#123;
    Message(-1, 'sha512校验失败')
  &#125;
&#125;)

// 当开始检查更新的时候触发
autoUpdater.on('checking-for-update', () => &#123;
  log.info('开始检查更新')
  Message(0)
&#125;)

// 发现可更新数据时
autoUpdater.on('update-available', () => &#123;
  log.info('有更新')
  Message(1)
&#125;)

// 没有可更新数据时
autoUpdater.on('update-not-available', () => &#123;
  log.info('没有更新')
  Message(2)
&#125;)

// 下载监听
autoUpdater.on('download-progress', (progressObj) => &#123;
  Message(3, progressObj)
&#125;)

// 下载完成
autoUpdater.on('update-downloaded', () => &#123;
  log.info('下载完成')
  Message(4)
  setTimeout(() => &#123; // 重启更新提示1秒后在进行重启安装
    global.willQuitApp = true
    autoUpdater.quitAndInstall()
  &#125;, 1000)
&#125;)

export default function (data) &#123;
  log.info('Update', data)
  autoUpdater.setFeedURL(data.upDateUrl)
  autoUpdater.checkForUpdates().catch(err => &#123;
    log.info('网络连接问题', err)
    Message(5, err.code)
  &#125;)
&#125;</code></pre><h2>渲染进程显示更新状态</h2><p>在上面的更新弹窗中新增更新进度，其实就是接收主进程的更新状态做个展示：</p><pre><code><a-modal
  v-model:visible="upDateProgress.show"
  title="下载中"
  :closable="false"
  :maskClosable="false"
  :keyboard="false"
  :destroyOnClose="true"
  :footer="null"
>
  <a-progress :percent="upDateProgress.percent" status="active" />
</a-modal>

const message = proxy.$message
onMounted(() => &#123;
  window.ipcRenderer.on('renderer-updateMsg', (_, data) => &#123;
    switch (data.type) &#123;
      case -1:
        message.error(data.data)
        break
      case 0:
        message.info('正在检查更新')
        break
      case 1:
        message.destroy()
        message.success('已检查到新版本，开始下载')
        state.upDateProgress.show = true
        break
      case 2:
        message.destroy()
        message.success('无新版本')
        break
      case 3:
        state.upDateProgress.percent = data.data.percent.toFixed(1)
        break
      case 4:
        state.upDateProgress.show = false
        message.loading('重启更新中...', 1)
        break
      case 5:
        message.destroy()
        message.warning(data.data)
        state.upDateProgress.show = false
        break
      default:
        break
    &#125;
  &#125;)
&#125;)
onUnmounted(() => &#123;
  window.ipcRenderer.removeListener('renderer-updateMsg')
&#125;)</code></pre><p>开发完成后我们打个0.0.1版本的dev包（上面我们放入server文件夹的是0.0.2的dev包），然后检测更新，更新重启后看打印的config是否是0.0.2。</p><h2>补充</h2><p>通过上面的步骤，我们的一个全量更新的流程就算完成了，这里对一些常见问题进行补充。</p><h3>请求缓存</h3><p>我们的请求是一个json文件，我们可能会修改其中的参数，有时候发现返回还是没变，请将控制台的<code>Network</code>的<code>Disable cache</code>勾上（请求缓存常见处理方式）</p><h3>下载缓存</h3><p>在开发时我们可能会做开发调试，比如看下载进度呀什么的，先打了一个高版本的放在远程地址，本地重复安装低版本的看更新效果，但是在第一次更新完成后，后面的更新都是瞬间完成了，看不到进度，这里是由于<code>electron-updater</code>在更新时会检测本地是否下载过这个高版本，有的话直接用本地的进行安装，我们可以把这个缓存文件删除掉。AppData这个文件夹呢可能是处于隐藏的，后面挺多地方会用到这个的，可以在顶端查看中勾选隐藏的项目让其显示，具体的话百度吧。</p><pre><code>electronvuedev这个是你设置的name（本框架在vue.config.js中）
win：C:\Users\Administrator（你的用户）\AppData\Local\electronvuedev-updater
mac：~/Library/Application Support/Caches/electronvuedev-updater</code></pre><h3>更新错误检测</h3><p>有时候我们更新时会遇到问题，比如检测出更新，但是下载却不动，或是更新完成后并没有安装重启，这里先说一下比较常见的几个可能会引发的问题</p><ul><li>mac端下载进度不动：mac端打包会出现三个文件，dmg安装包，dmg的zip压缩包以及yml件，比win多一个zip压缩包，mac更新下载的是zip文件，很多同学以为和win的exe一样放（win是exe和yml），把dmg文件放到更新地址下，没有zip文件，这会导致检测到更新，但下载进度却不动。</li><li>更新下载后没有重启，打开软件版本也没有变：之前我们在做窗口关闭时说过，可以在某些事件里用<code>e.preventDefault()</code>阻止窗口的关闭，比如我们在第二期里使用了：</li></ul><pre><code>win.on('close', (e) => &#123;
  console.log('close', global.willQuitApp)
  if (!global.willQuitApp) &#123;
    win.webContents.send('renderer-close-tips', &#123; isMac &#125;)
    e.preventDefault()
  &#125;
&#125;)</code></pre><p>针对于本项目，我们在调用重启更新时，由于我们设置了这个可能会引起窗口关闭的失败，这里我们在关闭前设置<code>willQuitApp</code>，让其正常关闭：</p><pre><code>global.willQuitApp = true
autoUpdater.quitAndInstall()</code></pre><ul><li><p>其他原因排查：当然不可能只有上面几种原因的，那么我们如何进行排查呢:</p><ul><li>后端错误收集：autoUpdater的error事件，可以在这个事件中把错误信息传递给后端接口。</li><li>添加错误日志：如果只能自己调试的话，可以用<code>electron-log</code>这个包把autoUpdater的error收集到本地日志中：</li></ul><pre><code>npm i electron-log

新建log.js
import log from 'electron-log'

log.transports.file.level = 'silly'
log.transports.console.level = false // 禁用console输出

export default log

在我们的checkUpdate.js更新中使用
import log from '../config/log.js'
autoUpdater.logger = log

autoUpdater.on('error', (err) => &#123;
  log.info('更新出现错误')
  log.info(err.message)
&#125;)</code></pre><p>当更新出现问题后查看对应的log文件</p><pre><code>win：C:\Users\Administrator（你的用户）\AppData\Roaming\<app name>\logs
mac: ~/Library/Logs/<app name></code></pre></li></ul><p>本系列更新只有利用周末和下班时间整理，比较多的内容的话更新会比较慢，希望能对你有所帮助，请多多star或点赞收藏支持一下</p><p>本文地址：<a href="https://xuxin123.com/%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E7%9A%84electron%E5%BC%80%E5%8F%91-%E6%9B%B4%E6%96%B0-%E5%85%A8%E9%87%8F%E6%9B%B4%E6%96%B0/" rel="nofollow">链接</a>  <br>本文github地址：<a href="https://github.com/xuxingeren/vue-cli-electron" rel="nofollow">链接</a></p>  
</div>
            