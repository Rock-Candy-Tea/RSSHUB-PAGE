
---
title: 'Apache Commons Geometry 1.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9061'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9061'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Commons Geometry 是一个用于几何处理的通用 Java 库。该代码起源于 commons-math 项目的 <code>org.apache.commons.math3.geometry</code> 包， 但为了更好的可维护性被拉到一个单独的项目中。从那以后，它经历了许多改进，包括对核心接口和类的重大重构。</p> 
<p>Apache Commons Geometry 1.0 正式发布，更新内容如下：</p> 
<h3>新特性：</h3> 
<ul> 
 <li>GEOMETRY-118: 添加特定坐标的转换方法到 <code>AffineTransformMatrixXD</code> 类，例如 "applyX"、"applyY"、"applyZ"；</li> 
 <li>GEOMETRY-95: 增加实体几何学教程；</li> 
 <li>GEOMETRY-120: 添加 <code>SimpleTriangleMeshBuilder.addFace(int[])</code> 方法作为替代 <code>addFace(int, int, int)</code>；</li> 
 <li>GEOMETRY-117: 为 AffineTransformMatrix2D 添加 <code>shear</code> 方法；</li> 
 <li>GEOMETRY-119: 添加 <code>VectorXD.normalizeOrNull()</code> 方法，以便调用者能够 检测规范化的失败，而不需要捕捉异常；</li> 
 <li>GEOMETRY-115: 为 IO 功能添加模块：commons-geometry-io-core, commons-geometry-io-euclidean；</li> 
 <li>GEOMETRY-108: 增加 BoundaryList 接口和实现类；</li> 
</ul> 
<h3>错误修复：</h3> 
<ul> 
 <li>GEOMETRY-116: 修复了不正确的 OSGi headers；</li> 
</ul> 
<h3>变化：</h3> 
<ul> 
 <li>GEOMETRY-138: 不要在 IO 模块中使用检查过的异常；</li> 
 <li>GEOMETRY-13: 使用 Commons Numbers 的 Norms.EUCLIDEAN 来计算 3D Euclidean 规范值；</li> 
 <li>GEOMETRY-126: 用 <code>VectorXD.Sum</code> 类替换 <code>VectorXD.linearCombination</code> 方法，使用 Commons Numbers 的 Sum 类来计算内部线性组合；</li> 
 <li>GEOMETRY-124: 将 DoublePrecisionContext 替换成 Precision.DoubleEquivalence；</li> 
 <li>GEOMETRY-109: 将 <code>BoundarySourceXX.from()</code> static factory 方法更名为"of"，以更好地匹配 JDK 的 Stream.of() 方法；</li> 
 <li>GEOMETRY-103: 将单元测试迁移到 JUnit 5；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcommons.apache.org%2Fproper%2Fcommons-geometry%2Fchanges-report.html" target="_blank">https://commons.apache.org/proper/commons-geometry/changes-report.html</a></p>
                                        </div>
                                      
</div>
            