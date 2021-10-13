
---
title: '【iOS】仿喜马拉雅首页背景颜色渐变效果'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1598505-9a09d8737ea6e0d8.gif'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1598505-9a09d8737ea6e0d8.gif'
---

<div>   
<h2>前言</h2>
<p>之前公司要求实现喜马拉雅的首页背景颜色渐变效果，于是花了一段时间实现了出来，在这里记录下，实现该效果主要用到了下面两个库：<br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fpujiaxin33%2FJXCategoryView" target="_blank">JXCategoryView</a>一个功能强大的分类控件<br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FQuintGao%2FGKCycleScrollView" target="_blank">GKCycleScrollView</a>我自己写的一个轮播图控件</p>
<h2>效果图</h2>
<p>先来看下效果图：</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="400" data-height="640"><img data-original-src="//upload-images.jianshu.io/upload_images/1598505-9a09d8737ea6e0d8.gif" data-original-width="400" data-original-height="640" data-original-format="image/gif" data-original-filesize="5523702" src="https://upload-images.jianshu.io/upload_images/1598505-9a09d8737ea6e0d8.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">xmly.gif</div>
</div>
<h2>说明</h2>
<p>通过研究喜马拉雅首页你会发现，要实现该功能有三个地方需要注意<br>
1、轮播图的滑动（左右滑动背景颜色根据图片渐变）<br>
2、分类切换页面（两个页面的当前背景色渐变）<br>
3、页面上下滑动（滑动到临界位置后背景色不再根据轮播图变化）<br>
下面来说明下实现过程<br>
<code>JXCategoryView</code>里面有个方法，传入两个颜色及渐变百分比，返回对应的渐变颜色，这里直接用这个方法实现渐变</p>
<h6>1、轮播图滑动</h6>
<p>轮播图用的<code>GKCycleScrollView</code>,需要监听UIScrollView的滑动，根据滑动的距离和方向，计算出当前图片和下一张图片以及渐变百分比，下面看下具体代码：</p>
<pre><code>// 滑动渐变背景色
- (void)cycleScrollView:(GKCycleScrollView *)cycleScrollView didScroll:(UIScrollView *)scrollView &#123;
    if (self.isCriticalPoint) return;
    
    CGFloat offsetX = scrollView.contentOffset.x;
    CGFloat maxW = self.bannerLists.count * scrollView.bounds.size.width;
    
    CGFloat changeOffsetX = offsetX - maxW;
    
    BOOL isFirstRight = NO;
    
    if (changeOffsetX < 0) &#123;
        changeOffsetX = -changeOffsetX;
        isFirstRight = YES;
    &#125;
    
    CGFloat ratio = (changeOffsetX / scrollView.bounds.size.width);
    
    // 超过了边界，不需要处理
    if (ratio > self.bannerLists.count || ratio < 0) return;
    
    ratio = MAX(0, MIN(self.bannerLists.count, ratio));
    
    NSInteger baseIndex = floorf(ratio);
    
    // 最后一个
    if (baseIndex + 1 > self.bannerLists.count) &#123;
        baseIndex = 0;
    &#125;
    
    CGFloat remainderRatio = ratio - baseIndex;
    if (remainderRatio <= 0 || remainderRatio >= 1) return;
    
    GKHomeBannerModel *leftModel  = self.bannerLists[baseIndex];
    
    NSInteger nextIndex = 0;
    if (isFirstRight) &#123;
        nextIndex = self.bannerLists.count - 1;
    &#125;else if (baseIndex == self.bannerLists.count - 1) &#123;
        nextIndex = 0;
    &#125;else &#123;
        nextIndex = baseIndex + 1;
    &#125;
    
    GKHomeBannerModel *rightModel = self.bannerLists[nextIndex];
    
    UIColor *leftColor  = leftModel.headerBgColor ? leftModel.headerBgColor : GKHomeBGColor;
    UIColor *rightColor = rightModel.headerBgColor ? rightModel.headerBgColor : GKHomeBGColor;
    
    UIColor *color = [JXCategoryFactory interpolationColorFrom:leftColor to:rightColor percent:remainderRatio];
    
    self.bgColor = color;
    
    if (self.isSelected && [self.delegate respondsToSelector:@selector(listVC:didChangeColor:)]) &#123;
        [self.delegate listVC:self didChangeColor:color];
    &#125;
&#125;
</code></pre>
<h6>2、分类切换页面</h6>
<p>监听JXCategoryView的delegate方法，根据滑动距离找出当前页面和下一个页面及滑动百分比，渐变背景颜色</p>
<pre><code>- (void)categoryView:(JXCategoryBaseView *)categoryView scrollingFromLeftIndex:(NSInteger)leftIndex toRightIndex:(NSInteger)rightIndex ratio:(CGFloat)ratio &#123;
    
    GKListViewController *leftVC  = (GKListViewController *)self.containerView.validListDict[@(leftIndex)];
    GKListViewController *rightVC = (GKListViewController *)self.containerView.validListDict[@(rightIndex)];
    
    UIColor *leftColor  = leftVC.isCriticalPoint ? [UIColor whiteColor] : leftVC.bgColor;
    UIColor *rightColor = rightVC.isCriticalPoint ? [UIColor whiteColor] : rightVC.bgColor;
    
    UIColor *color = [JXCategoryFactory interpolationColorFrom:leftColor to:rightColor percent:ratio];
    
    self.headerBgView.backgroundColor = color;
    
    // 两边状态一样，不用改变
    if (leftVC.isCriticalPoint == rightVC.isCriticalPoint) return;
    
    if (leftVC.isCriticalPoint) &#123;
        if (ratio > 0.5) &#123;
            [self changeToWhiteStateAtVC:nil];
        &#125;else &#123;
            [self changeToBlackStateAtVC:nil];
        &#125;
    &#125;else if (rightVC.isCriticalPoint) &#123;
        if (ratio > 0.5) &#123;
            [self changeToBlackStateAtVC:nil];
        &#125;else &#123;
            [self changeToWhiteStateAtVC:nil];
        &#125;
    &#125;
&#125;
</code></pre>
<h6>3、页面上下滑动</h6>
<p>监听列表的上下滑动，根据滑动距离判断是否到底临界点，改变分类的背景色</p>
<pre><code>- (void)listVC:(GKListViewController *)vc didScroll:(UIScrollView *)scrollView &#123;
    if (self.style == GKHomeThemeStyleNone) return;
    
    CGFloat offsetY = scrollView.contentOffset.y;
    if (offsetY <= 0) return;
    
    if (offsetY > ADAPTATIONRATIO * 360.0f) &#123;
        [self changeToBlackStateAtVC:vc];
    &#125;else &#123;
        [self changeToWhiteStateAtVC:vc];
    &#125;
&#125;
</code></pre>
<h6>4、动态刷新标题颜色和指示器颜色</h6>
<p>关于动态改变标题颜色、指示器颜色<code>JXCategoryView</code>并没有提供相关方法，于是通过查看相关代码，找到了下面的解决办法，通过对<code>JXCategoryTitleView</code>添加分类实现</p>
<pre><code>- (void)refreshCellState &#123;
    [self.dataSource enumerateObjectsUsingBlock:^(JXCategoryBaseCellModel * _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) &#123;
        [self reloadCellAtIndex:idx];
    &#125;];
    
    CGRect selectedCellFrame = CGRectZero;
    JXCategoryIndicatorCellModel *selectedCellModel = nil;
    for (int i = 0; i < self.dataSource.count; i++) &#123;
        JXCategoryIndicatorCellModel *cellModel = (JXCategoryIndicatorCellModel *)self.dataSource[i];
        cellModel.sepratorLineShowEnabled = self.isSeparatorLineShowEnabled;
        cellModel.separatorLineColor = self.separatorLineColor;
        cellModel.separatorLineSize = self.separatorLineSize;
        cellModel.backgroundViewMaskFrame = CGRectZero;
        cellModel.cellBackgroundColorGradientEnabled = self.isCellBackgroundColorGradientEnabled;
        cellModel.cellBackgroundSelectedColor = self.cellBackgroundSelectedColor;
        cellModel.cellBackgroundUnselectedColor = self.cellBackgroundUnselectedColor;
        if (i == self.dataSource.count - 1) &#123;
            cellModel.sepratorLineShowEnabled = NO;
        &#125;
        if (i == self.selectedIndex) &#123;
            selectedCellModel = cellModel;
            selectedCellFrame = [self getTargetCellFrame:i];
        &#125;
    &#125;
    
    for (UIView<JXCategoryIndicatorProtocol> *indicator in self.indicators) &#123;
        if (self.dataSource.count <= 0) &#123;
            indicator.hidden = YES;
        &#125;else &#123;
            indicator.hidden = NO;
            JXCategoryIndicatorParamsModel *indicatorParamsModel = [[JXCategoryIndicatorParamsModel alloc] init];
            indicatorParamsModel.selectedIndex = self.selectedIndex;
            indicatorParamsModel.selectedCellFrame = selectedCellFrame;
            [indicator jx_refreshState:indicatorParamsModel];
        &#125;
    &#125;
&#125;
</code></pre>
<p>到这里主要的功能点就已经实现了，当然还有很多细节，如果想了解，可以到github 上查阅相关代码。</p>
<h2>最后</h2>
<p>仿喜马拉雅首页背景颜色渐变效果很多APP都在用，如果你需要的话可以在<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FQuintGao%2FGKXimalaya" target="_blank">GKXimalaya</a>中查看<br>
如果您觉得还不错，还请点个star，您的支持是我最大的动力。</p>
  
</div>
            