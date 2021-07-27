
---
title: 'react native 实现灵活的滑块组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d5362cadd644adb8bb1796732ef823~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 00:47:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d5362cadd644adb8bb1796732ef823~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">组件结构：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d5362cadd644adb8bb1796732ef823~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210727160057623" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">滑块底部组件：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4dbda2ae82744cc8b5551936fb407a9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210727164026987" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">PanResponder：</h4>
<blockquote>
<p>React-native手势处理：参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactnative.cn%2Fdocs%2Fpanresponder" target="_blank" rel="nofollow noopener noreferrer" title="https://reactnative.cn/docs/panresponder" ref="nofollow noopener noreferrer">reactnative.cn/docs/panres…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6df63fbc21334f55a6a13bc97bbc1fb0~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210727164057013" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">LinearGradient:</h4>
<blockquote>
<p>react-native-linear-gradient 支持渐变颜色的组件</p>
</blockquote>
<h3 data-id="heading-4">滑块按钮组件：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6d3c03e203b4dd2b90382b684d43152~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210727164127105" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">PanResponder:</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b017cdc1679346c1bb4b314720198206~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210727164207519" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">滑块加减组件：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcf516273ac1437c9d01ba3d9fa14872~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210727164253807" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">完整组件源码：</h3>
<pre><code class="copyable">import React, &#123;
  forwardRef,
  useEffect,
  useImperativeHandle,
  useMemo,
  useRef,
  useState,
&#125; from "react";
import &#123; View, Image, PanResponder, Text &#125; from "react-native";
import LinearGradient from "react-native-linear-gradient";
import IMAGES_WATERHEATEDBED from "../assets/images";
/**
 * 传值
 */
type SliderBarProps = &#123;
  max?: number;
  min?: number;
  step?: number;
  value?: number;
  onChange?: (num: number) => void;
  onPanResponderRelease?: (num: number) => void;
  onPanResponderMove?: (num: number) => void;
  resetValue?: (reset: (value: number) => void) => void;
  finalChange?: (num: number) => void;
&#125;;
​
/**
 * 对外导出控制方法
 */
export type SliderBarRef = &#123;
  setValue: (num: number) => void;
&#125;;
const SliderBar: React.ForwardRefRenderFunction<SliderBarRef, SliderBarProps> =
  (props, ref) => &#123;
    /**
     * 滑块按钮距离左边的距离
     */
    const [sliderbtnDistance, setSliderbtnDistance] = useState(0);
    /**
     * 按钮是否正在滑动
     */
    const [sliderBtnMoving, setSliderBtnMoving] = useState(false);
    /**
     * 滑块按钮的宽度
     */
    const sliderBtnWidth = useRef<number>(32);
    /**
     * 滑块的宽度
     */
    const sliderWidth = useRef<number>(210 - sliderBtnWidth.current);
    /**
     * 默认值
     */
    const &#123; max = 100, min = 0, step = 1, value = min &#125; = props;
    /**
     * 对外导出的持久化数据num
     */
    let finalNumRef = useRef<number>(0);
    /**
     * 滑块的步长
     */
    const sliderStep = useMemo(
      () => (step / (max - min)) * sliderWidth.current,
      [step, sliderWidth]
    );
​
    /**
     * 根据传值转换为滑块的滑动距离
     * @param v
     * @returns
     */
    const valueToSliderDistance = (v: number) => &#123;
      return ((v - min) / step) * sliderStep;
    &#125;;
​
    /**
     * 滑块变化
     * @param num
     * @returns
     */
    const changeSliderDistance = (num: number) => &#123;
      return new Promise<void>((reslove) => &#123;
        let distance: number = num;
        if (num <= 0) &#123;
          distance = 0;
        &#125;
        if (num >= sliderWidth.current) &#123;
          distance = sliderWidth.current;
        &#125;
        const percentage = (100 / sliderWidth.current) * distance;
        finalNumRef.current = parseInt(
          ((percentage / 100) * (max - min) + min).toFixed(0)
        );
        setSliderbtnDistance(distance);
        reslove();
      &#125;);
    &#125;;
​
    /**
     * sliderBtn滑动响应
     */
    const SliderBtnResponder = PanResponder.create(&#123;
      // 要求成为响应者：
      onStartShouldSetPanResponder: () => true,
      onStartShouldSetPanResponderCapture: () => true,
      onMoveShouldSetPanResponder: () => true,
      onMoveShouldSetPanResponderCapture: () => true,
      onPanResponderMove: (evt, gestureState) => &#123;
        // 最近一次的移动距离为gestureState.move&#123;X,Y&#125;
        // 从成为响应者开始时的累计手势移动距离为gestureState.d&#123;x,y&#125;
        changeSliderDistance(sliderbtnDistance + gestureState.dx);
        setSliderBtnMoving(true);
        props.onPanResponderMove?.(finalNumRef.current);
      &#125;,
      onPanResponderTerminationRequest: () => true,
      onPanResponderRelease: () => &#123;
        // 用户放开了所有的触摸点，且此时视图已经成为了响应者。
        // 一般来说这意味着一个手势操作已经成功完成。
        console.log("滑动结束");
        setSliderBtnMoving(false);
        // props.onPanResponderRelease?.(finalNum);
        props.finalChange?.(finalNumRef.current);
      &#125;,
      onPanResponderTerminate: () => &#123;
        // 另一个组件已经成为了新的响应者，所以当前手势将被取消。
      &#125;,
      onShouldBlockNativeResponder: () => &#123;
        // 返回一个布尔值，决定当前组件是否应该阻止原生组件成为JS响应者
        // 默认返回true。目前暂时只支持android。
        return true;
      &#125;,
    &#125;);
​
    /**
     * slider滑动响应
     */
    const SliderResponder = PanResponder.create(&#123;
      // 要求成为响应者：
      onStartShouldSetPanResponder: () => true,
      onStartShouldSetPanResponderCapture: () => true,
      onMoveShouldSetPanResponder: () => true,
      onMoveShouldSetPanResponderCapture: () => true,
​
      onPanResponderGrant: (evt) => &#123;
        // 开始手势操作。给用户一些视觉反馈，让他们知道发生了什么事情！
        changeSliderDistance(evt.nativeEvent.locationX);
      &#125;,
      onPanResponderTerminationRequest: () => true,
      onPanResponderRelease: () => &#123;
        // 用户放开了所有的触摸点，且此时视图已经成为了响应者。
        // 一般来说这意味着一个手势操作已经成功完成。
        console.log("滑动结束");
        setSliderBtnMoving(false);
        // props.onPanResponderRelease?.(finalNum);
        props.finalChange?.(finalNumRef.current);
      &#125;,
      onPanResponderTerminate: () => &#123;
        // 另一个组件已经成为了新的响应者，所以当前手势将被取消。
      &#125;,
      onShouldBlockNativeResponder: () => &#123;
        // 返回一个布尔值，决定当前组件是否应该阻止原生组件成为JS响应者
        // 默认返回true。目前暂时只支持android。
        return true;
      &#125;,
    &#125;);
​
    /**
     * 父组件控制子组件回调
     */
    useImperativeHandle(ref, () => &#123;
      return &#123;
        setValue(v) &#123;
          console.log("调用子组件");
          changeSliderDistance(valueToSliderDistance(v));
        &#125;,
      &#125;;
    &#125;);
​
    useEffect(() => &#123;
      console.log("======", finalNumRef.current);
      props.onChange?.(finalNumRef.current);
      return () => &#123;&#125;;
    &#125;, [finalNumRef.current]);
​
    /**
     * 初始化
     */
    useEffect(() => &#123;
      changeSliderDistance(valueToSliderDistance(value));
      props.resetValue?.((v) => &#123;
        changeSliderDistance(valueToSliderDistance(v));
      &#125;);
      return () => &#123;&#125;;
    &#125;, [value, sliderStep, step]);
​
    return (
      <View
        style=&#123;&#123;
          marginTop: 37,
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
        &#125;&#125;
      >
        &#123;/* 滑块组件 */&#125;
        <View
          style=&#123;&#123;
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
          &#125;&#125;
        >
          &#123;/* 滑块底部组件 */&#125;
          <View
            &#123;...SliderResponder.panHandlers&#125;
            style=&#123;&#123;
              width: 210,
              height: 22,
              backgroundColor: "#F8F8F8",
              borderRadius: 11,
              borderWidth: 2,
              borderStyle: "solid",
              borderColor: "#fff",
              display: "flex",
              alignItems: "flex-start",
              justifyContent: "center",
              paddingHorizontal: 6,
              position: "relative",
              marginRight: 16,
            &#125;&#125;
          >
            <LinearGradient
              start=&#123;&#123; x: 0, y: 0 &#125;&#125;
              end=&#123;&#123; x: 1, y: 0 &#125;&#125;
              colors=&#123;["#F0A64D", "#F78240"]&#125;
              style=&#123;&#123;
                width: sliderbtnDistance, // 滑块按钮距离左边的距离
                height: 10,
                borderRadius: 5,
              &#125;&#125;
            />
          </View>
          &#123;/* 滑块按钮组件 */&#125;
          <View
            &#123;...SliderBtnResponder.panHandlers&#125;
            style=&#123;&#123;
              position: "absolute",
              left: sliderbtnDistance,
              transform: [&#123; scale: sliderBtnMoving ? 1.2 : 1 &#125;],
            &#125;&#125;
          >
            <View
              style=&#123;&#123;
                opacity: sliderBtnMoving ? 1 : 0,
                position: "absolute",
                top: -24,
                left: -((35 - sliderBtnWidth.current) / 2),
                width: 35,
                height: 24,
              &#125;&#125;
            >
              <Image
                style=&#123;&#123; position: "absolute", left: 0, top: 0 &#125;&#125;
                source=&#123;IMAGES_WATERHEATEDBED.bubble&#125;
              />
​
              <Text
                style=&#123;&#123;
                  fontSize: 14,
                  lineHeight: 20,
                  color: "#fff",
                  width: "100%",
                  textAlign: "center",
                &#125;&#125;
              >&#123;`$&#123;finalNumRef.current&#125;`&#125;</Text>
            </View>
            <Image source=&#123;IMAGES_WATERHEATEDBED.slider_btn&#125; />
          </View>
        </View>
        &#123;/* 滑块加减组件 */&#125;
        <View
          style=&#123;&#123;
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
          &#125;&#125;
        >
          <View
            onTouchStart=&#123;() => &#123;
              changeSliderDistance(sliderbtnDistance - sliderStep).then(() =>
                props.finalChange?.(finalNumRef.current)
              );
            &#125;&#125;
            style=&#123;&#123; marginRight: 9 &#125;&#125;
          >
            <Image source=&#123;IMAGES_WATERHEATEDBED.slider_icon_left&#125; />
          </View>
          <View
            onTouchStart=&#123;() => &#123;
              changeSliderDistance(sliderbtnDistance + sliderStep).then(() =>
                props.finalChange?.(finalNumRef.current)
              );
            &#125;&#125;
          >
            <Image source=&#123;IMAGES_WATERHEATEDBED.slider_icon_right&#125; />
          </View>
        </View>
      </View>
    );
  &#125;;
​
export default forwardRef(SliderBar);
​
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            