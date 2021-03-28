
---
title: 'Vue3 生成图片验证码组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8034'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 01:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8034'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>突然用到图片验证码，从其他论坛上东拼西凑出本地前端生成验证码图片的组件，做一下笔记。</p>
<h4 data-id="heading-0">1、安装依赖</h4>
<p>需要用到【identify】和【md5】</p>
<p>其中【md5】主要的作用是用于验证码正确值加密使用</p>
<pre><code class="copyable">npm install identify
npm install md5
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2、组件部分</h4>
<p>此处使用到canvas</p>
<pre><code class="copyable"><template>
 <div class="s-canvas">
  <canvas id="s-canvas" :width="contentWidth" :height="contentHeight"></canvas>
 </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">
<script>
import md5 from 'js-md5'
import &#123;
toRefs,
onMounted,
watch,
defineComponent
&#125; from 'vue'

export default defineComponent(&#123;
name: 'imageCode',
props: &#123;
change: &#123; // 刷新验证码使用
type: Boolean,
default: false
&#125;,
contentWidth: &#123; // 验证码图片宽
type: Number,
default: 112
&#125;,
contentHeight: &#123; // 验证码图片高
type: Number,
default: 38
&#125;
&#125;,
emits: ["getCode"], // 返回验证码加密正确值的函数
setup(props, context) &#123;
                        // 默认值 
const defaultData = &#123;
identifyCode: '', // 验证码值，未加密的
identifyCodes: '1234567890', // 生成验证码的元素，可以加入字母
fontSizeMin: 20, // 图片上验证文字的最小值
fontSizeMax: 40, // 图片上验证文字的最小值
backgroundColorMin: 180, // 图片背景色值最小
backgroundColorMax: 240, // 图片背景色值最大
colorMin: 50, // 文字色值最小
colorMax: 160, // 文字色值最大
lineColorMin: 40, // 干扰线色值最小
lineColorMax: 120, // 干扰线色值最大
dotColorMin: 0, // 干扰点色值最小
dotColorMax: 255, // 干扰点色值最大
                                lineSum: 4, // 干扰线数量
                                dotSum: 40, // 干扰点数量
&#125;
                        // 父级传递
const &#123;
contentWidth,
contentHeight,
change
&#125; = toRefs(props)

// 生成一个随机数
const randomNum = (min, max) => &#123;
return Math.floor(Math.random() * (max - min) + min)
&#125;

// 生成一个随机的颜色
const randomColor = (min, max) => &#123;
let r = randomNum(min, max)
let g = randomNum(min, max)
let b = randomNum(min, max)
return 'rgb(' + r + ',' + g + ',' + b + ')'
&#125;

// 创建图形
const drawPic = () => &#123;
let canvas = document.getElementById('s-canvas')
let ctx = canvas.getContext('2d')
ctx.textBaseline = 'bottom'
// 绘制背景
ctx.fillStyle = randomColor(defaultData.backgroundColorMin, defaultData.backgroundColorMax)
ctx.fillRect(0, 0, contentWidth.value, contentHeight.value)
// 绘制文字
for (let i = 0; i < defaultData.identifyCode.length; i++) &#123;
drawText(ctx, defaultData.identifyCode[i], i)
&#125;
drawLine(ctx)
drawDot(ctx)
&#125;

// 绘制文字
const drawText = (ctx, txt, i) => &#123;
ctx.fillStyle = randomColor(defaultData.colorMin, defaultData.colorMax)
ctx.font = randomNum(defaultData.fontSizeMin, defaultData.fontSizeMax) + 'px SimHei'
let x = (i + 1) * (contentWidth.value / (defaultData.identifyCode.length + 1))
let y = randomNum(defaultData.fontSizeMax, contentHeight.value - 5)
var deg = randomNum(-45, 45)
// 修改坐标原点和旋转角度
ctx.translate(x, y)
ctx.rotate(deg * Math.PI / 180)
ctx.fillText(txt, 0, 0)
// 恢复坐标原点和旋转角度
ctx.rotate(-deg * Math.PI / 180)
ctx.translate(-x, -y)
&#125;

// 绘制干扰线
const drawLine = (ctx) => &#123;
for (let i = 0; i < 4; i++) &#123;
ctx.strokeStyle = randomColor(defaultData.lineColorMin, defaultData.lineColorMax)
ctx.beginPath()
ctx.moveTo(randomNum(0, contentWidth.value), randomNum(0, contentHeight.value))
ctx.lineTo(randomNum(0, contentWidth.value), randomNum(0, contentHeight.value))
ctx.stroke()
&#125;
&#125;
// 绘制干扰点
const drawDot = (ctx) => &#123;
for (let i = 0; i < 60; i++) &#123;
ctx.fillStyle = randomColor(0, 255)
ctx.beginPath()
ctx.arc(randomNum(0, contentWidth.value), randomNum(0, contentHeight.value), 1, 0, 2 * Math
.PI)
ctx.fill()
&#125;
&#125;

// 生成图片
const makeCode = () => &#123;
defaultData.identifyCode = "";
for (let i = 0; i < 4; i++) &#123;
defaultData.identifyCode += defaultData.identifyCodes[
randomNum(0, defaultData.identifyCodes.length)
];
&#125;
                                
                                // 绘制图片
drawPic()
                                // 返回加密后的图片验证码值
context.emit('getCode', md5(defaultData.identifyCode))
&#125;
                        
                        // 初识函数，生成图片 
onMounted(() => &#123;
makeCode()
&#125;)

                        // 监听change变化，重新生成图片
watch(change, () => &#123;
makeCode()
&#125;)

&#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3、调用组件</h4>
<h5 data-id="heading-3">1、引入组件</h5>
<pre><code class="copyable">import imageCode from '../../../components/ImageCode.vue';
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">2、使用</h5>
<pre><code class="copyable"><image-code :change="data.change_img_code" @click="changeImageCode" @getCode="backImageCode"></image-code>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">3、script</h5>
<pre><code class="copyable">
export default &#123;
name: '',
components: &#123;
imageCode
&#125;,
setup()&#123;
const data = reactive(&#123;
change_img_code: false, // 刷新验证码
img_code:'',// 加密后的验证码值
&#125;)
                        
                        // 刷新验证码操作
const changeImageCode = ()=> &#123;
data.change_img_code = !data.change_img_code
&#125;

                        // 接收组件返回加密后的验证码值
const backImageCode = (code) =>&#123;
data.img_code = code
console.log('data',data.img_code)
&#125;

return &#123;
changeImageCode,
backImageCode,
data
&#125;
&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            