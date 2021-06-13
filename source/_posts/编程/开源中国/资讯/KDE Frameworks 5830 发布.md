
---
title: 'KDE Frameworks 5.83.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4502'
author: 开源中国
comments: false
date: Sun, 13 Jun 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4502'
---

<div>   
<div class="content">
                                                                    
                                                        <p>KDE Frameworks 5.80.0 已正式发布。KDE Frameworks 是 Qt 的 83 个附加库，它在成熟的、经过同行评审和测试的库中提供了各种常见的功能，并且具有友好的许可条款。</p> 
<h2><strong>主要更新内容</strong></h2> 
<ul> 
 <li> <h3>Baloo</h3> 
  <ul> 
   <li>在 KIOSlaves 中嵌入 JSON 元数据</li> 
   <li>将协议文件转换为 JSON</li> 
   <li>[balooctl] 允许清除已删除的文档</li> 
  </ul> </li> 
 <li> <h3>BluezQt</h3> 
  <ul> 
   <li>将缺少的 Qt5::DBus 添加到 qml 插件</li> 
  </ul> </li> 
 <li> <h3>Breeze Icons</h3> 
  <ul> 
   <li>再次添加了新的 KMyMoney 图标，并进行了一些额外的调整</li> 
   <li>添加 Goodvibes 图标</li> 
   <li>为 skanpage 添加图标</li> 
   <li>调整了 Rust 模拟类型以更好地匹配官方品牌（错误 434346）</li> 
   <li>使链接相对</li> 
   <li>更新图标并添加符号链接</li> 
   <li>分隔图标到 -left 和 -right</li> 
  </ul> </li> 
 <li> <h3>Extra CMake Modules</h3> 
  <ul> 
   <li>将 LicenseRef-KDE-Accepted-GPL 添加到许可证兼容性矩阵</li> 
   <li>ecm_gperf_generate()：为目标 arg 添加选项以添加 gen.source</li> 
   <li>ecm_qt_declare_logging_category：在内部失败之前捕获别名目标</li> 
   <li>添加模块以查找 libmount</li> 
   <li>删除 FindFontConfig.cmake</li> 
   <li>在尝试复制文件之前确保目录路径存在</li> 
   <li>如果未明确设置，则尝试查找 Play 商店图标</li> 
   <li>为 MSVC 添加地址清理程序</li> 
   <li>ecm_create_qm_loader：支持目标作为替代参数</li> 
   <li>不要通过列表富文本元素，Google Play 无法处理这些</li> 
   <li>使用 Sphinx 4 修复文档构建</li> 
   <li>在 FindTaglib.cmake 中使用 pkg_check_modules</li> 
   <li>处理无文本标签</li> 
   <li>ECMAddAppIcon：支持目标作为参数</li> 
   <li>因缺少翻译元素而回退到英语</li> 
   <li>ECMSetupVersion：逐步淘汰已弃用的 *_VERSION_STRING CMake 变量</li> 
   <li>为翻译的元数据扩展 Android 语言映射</li> 
  </ul> </li> 
 <li> <h3>KActivitiesStats</h3> 
  <ul> 
   <li>tier 字段是错误的，而不是 subgroup 字段</li> 
  </ul> </li> 
 <li> <h3>KArchive</h3> 
  <ul> 
   <li>[KArchive] 对打开错误使用更好的措辞</li> 
   <li>为 ZLib 使用导入的目标</li> 
  </ul> </li> 
 <li> <h3>KCalendarCore</h3> 
  <ul> 
   <li>允许按类别（标签）对待办事项进行排序</li> 
   <li>在计算标准和 dst 阶段的过渡日期时使用 UTC 时间</li> 
   <li>删除 3 之前的 libical 的条件编译</li> 
   <li>修复 Compat-libical3-eGroupware.ics</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkde.org%2Fannouncements%2Fframeworks%2F5%2F5.83.0%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            