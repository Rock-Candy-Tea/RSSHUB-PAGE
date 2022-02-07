
---
title: 'ECS 中同类关联数据的处理 (blog.codingnow.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=237'
author: 技术头条
comments: false
date: 2022-02-07 06:10:15
thumbnail: 'https://picsum.photos/400/300?random=237'
---

<div>   
ECS 模式下最难处理的是同类 Component 之间有相互联系的情况。

最方便 ECS 处理的数据是相互独立的，每个数据单元都不和其它数据单元产生联系；如果多个数据单元会有故有的联系时，当可以把它们看作是同一个实体（Entity）下的不同组件（Component）时，那么就可以借用 Entity 的概念来处理它们。我们依旧可以按固定的次序去迭代这些数据。

但是，在复杂系统中，无可避免的，同类数据相互之间也可以产生联系。例如：场景管理中，节点之间有父子关系，计算节点的空间状态的过程对数据的遍历次序有要求。且计算过程还需要访问父节点的状态。解决这类需求是 ECS 框架的一大挑战。
    
</div>
            