
---
title: 'Mir 2.9 发布，Ubuntu 安全显示服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7987'
author: 开源中国
comments: false
date: Sun, 28 Aug 2022 01:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7987'
---

<div>   
<div class="content">
                                                                                            <p>Mir 是一套用于构建基于 Wayland 的 Shell 库。Mir 简化了 Shell 作者需要处理的复杂性：它提供了一个稳定的、经过良好测试的、高性能的平台，具有触控、鼠标和平板电脑输入、多显示器功能和安全的客户端-服务器通信。</p> 
<h3>ABI 摘要</h3> 
<ul> 
 <li>miral ABI 升级至 5</li> 
 <li>mircore ABI 升级至 2</li> 
 <li>miroil ABI 升级至 2</li> 
</ul> 
<h3>增强</h3> 
<ul> 
 <li>[Wayland] 实现 zwp_idle_inhibit_manager_v1</li> 
 <li>[Wayland] 实现zwlr_virtual_pointer_v1</li> 
 <li>[Wayland] 实现zwp_text_input_manager_v1</li> 
 <li>[Wayland] 将 wl_seat 提升到 v8，并实现高像素滚动</li> 
 <li>[Wayland平台] 改进连接失败的错误</li> 
 <li>[Wayland平台] 移植到 xdg-shell</li> 
 <li>[MirAL] 允许 <code>--add-wayland-extenions all</code></li> 
 <li>[MirAL] 允许服务器获得重复的字符串选项</li> 
 <li>[MirAL] 对 ExternalClientLauncher 的改进，不要强迫客户端自己分割命令行</li> 
 <li>[MirAL] 整理事件过滤的 API</li> 
 <li>[MirAL] 暴露 miral::Zone::id()</li> 
 <li>[MirAL] 重命名 CommandLineOption => ConfigurationOption</li> 
 <li>[gbm-kms] 为 nvidia 和 evdi 的 driver-quirks 增加默认值</li> 
 <li>[gbm-kms] 为 vc4-drm 和 v3d 添加默认的驱动查询</li> 
 <li>[mir-smoke-test-runner] 启用只在 Wayland 环境下工作的功能</li> 
</ul> 
<h3>修复错误</h3> 
<ul> 
 <li>[Wayland] 键盘输入后发送键盘修改器</li> 
 <li>[Wayland] wlr-screencopy-v1：按要求发送 <code>.damage</code> 事件</li> 
 <li>[Wayland] wlr-screencopy-v1：在 <code>.copy_with_damage</code> 请求中等待复制区域被损坏</li> 
 <li>[eglstream-kms] 当提交坏的 EGLStreams 时，杀掉客户端，而不是 Mir</li> 
 <li>[eglstream-kms] 处理 devnum_for_device 中的 EGL 错误</li> 
 <li>[test clients] 明确询问 GLESv2 上下文</li> 
 <li>对本地构建的依赖关系进行 CMake 清理</li> 
 <li>修复事件时间戳</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMirServer%2Fmir%2Freleases%2Ftag%2Fv2.9.0" target="_blank">https://github.com/MirServer/mir/releases/tag/v2.9.0</a></p>
                                        </div>
                                      
</div>
            