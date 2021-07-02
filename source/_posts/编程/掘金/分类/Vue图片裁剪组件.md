
---
title: 'Vue图片裁剪组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe0b222cc65476c8353931412872e15~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 01:40:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe0b222cc65476c8353931412872e15~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">示例：</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe0b222cc65476c8353931412872e15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>tip: 该组件基于vue-cropper二次封装</em></p>
<h3 data-id="heading-1">安装插件</h3>
<pre><code class="copyable">npm install vue-cropper

yarn add vue-cropper

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">写入封装的组件</h3>
<pre><code class="copyable"><!-- 简易图片裁剪组件 --- 二次封装 -->
<!-- 更多api https://github.com/xyxiao001/vue-cropper -->
<!-- 使用：传入图片 比例 显示隐藏。方法：监听底部按钮点击即可  ---更多props查询文档自行添加 -->

<template>
  <div v-if="value" :value="value" @input="val => $emit('input', val)" class="conbox">
    <div class="info">
      <vueCropper
        ref="cropper"
        :img="img"
        :outputSize="outputSize"
        :outputType="outputType"
        :info="info"
        :canScale="canScale"
        :autoCrop="autoCrop"
        :fixed="fixed"
        :fixedNumber="fixedNumber"
        :full="full"
        :fixedBox="fixedBox"
        :canMove="canMove"
        :canMoveBox="canMoveBox"
        :original="original"
        :centerBox="centerBox"
        :infoTrue="infoTrue"
        :mode="mode"
      ></vueCropper>
    </div>
    <div class="btns">
      <div @click="clickCancelCut" class="cancel">取消</div>
      <img @click="clickRotate" src="../../assets/paradise/rotate.png" alt="" />
      <div @click="clickOk" class="okey">确定</div>
    </div>
  </div>
</template>

<script>
import &#123; VueCropper &#125; from 'vue-cropper';
export default &#123;
  name: 'PictureCropping',
  components: &#123; VueCropper &#125;,
  props: &#123;
    value: &#123;
      type: Boolean,
      default: false,
    &#125;,
    //裁剪图片的地址
    img: &#123;
      type: String,
      default: '',
    &#125;,
    //截图框的宽高比例
    fixedNumber: &#123;
      type: Array,
      default: () => &#123;
        return [1, 1];
      &#125;,
    &#125;,
  &#125;,
  data() &#123;
    return &#123;
      // 裁剪组件的基础配置option
      //   img: this.img, // 裁剪图片的地址
      outputSize: 1, // 裁剪生成图片的质量
      outputType: 'jpeg', // 裁剪生成图片的格式
      info: true, // 裁剪框的大小信息
      canScale: true, // 图片是否允许滚轮缩放
      autoCrop: true, // 是否默认生成截图框
      // autoCropWidth: 300, // 默认生成截图框宽度
      // autoCropHeight: 200, // 默认生成截图框高度
      fixed: true, // 是否开启截图框宽高固定比例
      //   fixedNumber: this.fixedNumber, // 截图框的宽高比例
      full: true, // 是否输出原图比例的截图
      fixedBox: true, // 固定截图框大小 不允许改变
      canMove: true, //上传图片是否可以移动
      canMoveBox: true, // 截图框能否拖动
      original: false, // 上传图片按照原始比例渲染
      centerBox: true, // 截图框是否被限制在图片里面
      // high:true,// 是否按照设备的dpr 输出等比例图片
      infoTrue: true, // true 为展示真实输出图片宽高 false 展示看到的截图框宽高
      // maxImgSize: 2000, //限制图片最大宽度和高度
      // enlarge: 1, //图片根据截图框输出比例倍数
      mode: 'contain', //图片默认渲染方式
    &#125;;
  &#125;,
  computed: &#123;&#125;,
  watch: &#123;&#125;,
  //生命周期 - 创建完成（访问当前this实例）
  created() &#123;&#125;,
  //生命周期 - 挂载完成（访问DOM元素）
  mounted() &#123;&#125;,
  methods: &#123;
    clickCancelCut() &#123;
      this.$emit('clickCancelCut', '点击取消');
      this.$refs.cropper.stopCrop();
      this.$refs.cropper.clearCrop();
    &#125;,
    clickRotate() &#123;
      this.$refs.cropper.rotateRight();
      this.$emit('clickRotate', '点击旋转');
    &#125;,
    clickOk() &#123;
      //输出裁剪的base64
      this.$refs.cropper.getCropData(data => &#123;
        this.$emit('clickOk', data);
        this.$refs.cropper.stopCrop();
        this.$refs.cropper.clearCrop();
      &#125;);
    &#125;,
  &#125;,
&#125;;
</script>
<style lang='less' scoped>
/* @import url(); 引入css类 */
.conbox &#123;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  box-sizing: border-box;
  height: 100vh;
  width: 100%;
  background-color: #000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  .info &#123;
    width: auto;
    height: 800px;
    .vue-cropper &#123;
      background-image: none;
      background-color: #000;
    &#125;
  &#125;
  .btns &#123;
    padding: 0 20px;

    color: #fff;
    text-align: center;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: absolute;
    left: 0;
    right: 0;
    bottom: 15px;
    img &#123;
      width: 85px;
      height: 85px;
    &#125;
    .cancel &#123;
      background-color: #606465;
      padding: 15px 20px;
      width: 100px;
      border-radius: 10px;
    &#125;
    .okey &#123;
      background-color: #df6457;
      padding: 15px 20px;
      width: 100px;
      border-radius: 10px;
    &#125;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            