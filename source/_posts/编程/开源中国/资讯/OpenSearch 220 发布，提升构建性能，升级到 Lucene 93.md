
---
title: 'OpenSearch 2.2.0 发布，提升构建性能，升级到 Lucene 9.3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3061'
author: 开源中国
comments: false
date: Sun, 07 Aug 2022 14:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3061'
---

<div>   
<div class="content">
                                                                                            <p>AWS OpenSearch 2.2.0 发布了，<span style="background-color:#ffffff; color:#333333">OpenSearch 是 AWS 自 Elasticsearch 7.10.2 的开源搜索和分析引擎。</span></p> 
<p>新版本改进内容包括：</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Features/Enhancements</h3> 
<ul> 
 <li>Task consumer Integration (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F2293">#2293</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4141">#4141</a>)</li> 
 <li>[Backport 2.x] [Segment Replication] Add SegmentReplicationTargetService to orchestrate replication events. (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4074">#4074</a>)</li> 
 <li>Support task resource tracking in OpenSearch (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3982">#3982</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4087">#4087</a>)</li> 
 <li>Making shard copy count a multiple of attribute count (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3462">#3462</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4086">#4086</a>)</li> 
 <li>[Backport 2.x] [Segment Rreplication] Adding CheckpointRefreshListener to trigger when Segment replication is turned on and Primary shard refreshes (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4044">#4044</a>)</li> 
 <li>Add doc_count field mapper (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3985">#3985</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4037">#4037</a>)</li> 
 <li>Parallelize stale blobs deletion during snapshot delete (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3796">#3796</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3990">#3990</a>)</li> 
 <li>[Backport 2.x] [Segment Replication] Add a new Engine implementation for replicas with segment replication enabled. (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4003">#4003</a>)</li> 
 <li>[Backport 2.x] Adds a new parameter, max_analyzer_offset, for the highlighter (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4031">#4031</a>)</li> 
 <li>Update merge on refresh and merge on commit defaults in Opensearch (Lucene 9.3) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3561">#3561</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4013">#4013</a>)</li> 
 <li>Make HybridDirectory MMAP Extensions Configurable (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3837">#3837</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3970">#3970</a>)</li> 
 <li>Add option to disable chunked transfer-encoding (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3864">#3864</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3885">#3885</a>)</li> 
 <li>Introducing TranslogManager implementations decoupled from the Engine [2.x] (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3820">#3820</a>)</li> 
 <li>Changing default no_master_block from write to metadata_write (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3621">#3621</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3756">#3756</a>)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Bug Fixes</h3> 
<ul> 
 <li>OpenSearch crashes on closed client connection before search reply when total ops higher compared to expected (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4143">#4143</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4145">#4145</a>)</li> 
 <li>Binding empty instance of SegmentReplicationCheckpointPublisher when Feature Flag is off in IndicesModule.java file. (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4119">#4119</a>)</li> 
 <li>Fix the bug that masterOperation(with task param) is bypassed (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4103">#4103</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4115">#4115</a>)</li> 
 <li>Fixing flaky org.opensearch.cluster.routing.allocation.decider.DiskThresholdDeciderIT.testHighWatermarkNotExceeded test case (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4012">#4012</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4014">#4014</a>)</li> 
 <li>Correct typo: Rutime -> Runtime (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3896">#3896</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3898">#3898</a>)</li> 
 <li>Fixing implausibly old time stamp 1970-01-01 00:00:00 by using the timestamp from the Git revision instead of default 0 value (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3883">#3883</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3891">#3891</a>)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Infrastructure</h3> 
<ul> 
 <li>Correctly ignore depandabot branches during push (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4077">#4077</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4113">#4113</a>)</li> 
 <li>Build performance improvements (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3926">#3926</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3937">#3937</a>)</li> 
 <li>PR coverage requirement and default settings (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3931">#3931</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3938">#3938</a>)</li> 
 <li>[Backport 2.x] Fail build on wildcard imports (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3940">#3940</a>)</li> 
 <li>Don't run EmptyDirTaskTests in a Docker container (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3792">#3792</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3912">#3912</a>)</li> 
 <li>Add coverage, gha, jenkins server, documentation and forum badges (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3886">#3886</a>)</li> 
 <li>Unable to use Systemd module with tar distribution (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3755">#3755</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3903">#3903</a>)</li> 
 <li>Ignore backport / autocut / dependentbot branches for gradle checks (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3816">#3816</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3825">#3825</a>)</li> 
 <li>Setup branch push coverage and fix coverage uploads (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3793">#3793</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3811">#3811</a>)</li> 
 <li>Enable XML test reports for Jenkins integration (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3799">#3799</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3803">#3803</a>)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Maintenance</h3> 
<ul> 
 <li>OpenJDK Update (July 2022 Patch releases) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4023">#4023</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4092">#4092</a>)</li> 
 <li>Update to Lucene 9.3.0 (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4043">#4043</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4088">#4088</a>)</li> 
 <li>Bump commons-configuration2 from 2.7 to 2.8.0 in /plugins/repository-hdfs (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3764">#3764</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3783">#3783</a>)</li> 
 <li>Use bash in systemd-entrypoint shebang (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4008">#4008</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4009">#4009</a>)</li> 
 <li>Bump com.gradle.enterprise from 3.10.1 to 3.10.2 (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3568">#3568</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3934">#3934</a>)</li> 
 <li>Bump log4j-core in /buildSrc/src/testKit/thirdPartyAudit/sample_jars (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3763">#3763</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3784">#3784</a>)</li> 
 <li>Added bwc version 1.3.5 (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3911">#3911</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3913">#3913</a>)</li> 
 <li>Update to Gradle 7.5 (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3594">#3594</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3904">#3904</a>)</li> 
 <li>Update Netty to 4.1.79.Final (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3868">#3868</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3874">#3874</a>)</li> 
 <li>Upgrade MinIO image version (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3541">#3541</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3867">#3867</a>)</li> 
 <li>Add netty-transport-native-unix-common to modules/transport-netty4/bu… (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3848">#3848</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3853">#3853</a>)</li> 
 <li>Update outdated dependencies (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3821">#3821</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3854">#3854</a>)</li> 
 <li>Added bwc version 2.1.1 (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3806">#3806</a>)</li> 
 <li>Upgrade netty from 4.1.73.Final to 4.1.78.Final (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3772">#3772</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3778">#3778</a>)</li> 
 <li>Bump protobuf-java from 3.21.1 to 3.21.2 in /plugins/repository-hdfs (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3711">#3711</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3726">#3726</a>)</li> 
 <li>Upgrading AWS SDK dependency for native plugins (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3694">#3694</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3701">#3701</a>)</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Refactoring</h3> 
<ul> 
 <li>[Backport 2.x] Changes to encapsulate Translog into TranslogManager (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4095">#4095</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4142">#4142</a>)</li> 
 <li>Deprecate and rename abstract methods in interfaces that contain 'master' in name (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4121">#4121</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4123">#4123</a>)</li> 
 <li>[Backport 2.x] Integrate Engine with decoupled Translog interfaces (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3822">#3822</a>)</li> 
 <li>Deprecate class FakeThreadPoolMasterService, BlockMasterServiceOnMaster and BusyMasterServiceDisruption (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4058">#4058</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4068">#4068</a>)</li> 
 <li>Rename classes with name 'MasterService' to 'ClusterManagerService' in directory 'test/framework' (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4051">#4051</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4057">#4057</a>)</li> 
 <li>Deprecate class 'MasterService' and create alternative class 'ClusterManagerService' (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4022">#4022</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4050">#4050</a>)</li> 
 <li>Deprecate and Rename abstract methods from 'Master' terminology to 'ClusterManager'. (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4032">#4032</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4048">#4048</a>)</li> 
 <li>Deprecate public methods and variables that contain 'master' terminology in class 'NoMasterBlockService' and 'MasterService' (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4006">#4006</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F4038">#4038</a>)</li> 
 <li>Deprecate public methods and variables that contain 'master' terminology in 'client' directory (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3966">#3966</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3981">#3981</a>)</li> 
 <li>[segment replication]Introducing common Replication interfaces for segment replication and recovery code paths (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3234">#3234</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3984">#3984</a>)</li> 
 <li>Deprecate public methods and variables that contain 'master' terminology in 'test/framework' directory (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3978">#3978</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3987">#3987</a>)</li> 
 <li>[Backport 2.x] [Segment Replication] Moving RecoveryState.Index to a top-level class and renaming (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3971">#3971</a>)</li> 
 <li>Rename and deprecate public methods that contains 'master' in the name in 'server' directory (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3647">#3647</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3964">#3964</a>)</li> 
 <li>[2.x] Deprecate public class names with master terminology (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3871">#3871</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3914">#3914</a>)</li> 
 <li>[Backport 2.x] Rename public classes with 'Master' to 'ClusterManager' (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3870">#3870</a>)</li> 
 <li>Revert renaming masterOperation() to clusterManagerOperation() (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3681">#3681</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3714">#3714</a>)</li> 
 <li>Revert renaming method onMaster() and offMaster() in interface LocalNodeMasterListener (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3686">#3686</a>) (<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fopensearch-project%2Fopensearch%2Fpull%2F3693">#3693</a>)</li> 
</ul> 
<p>详细每个版本的改进内容请看</p> 
<p><a href="https://gitee.com/mirrors/OpenSearch-Project/tree/main/release-notes">https://gitee.com/mirrors/OpenSearch-Project/tree/main/release-note</a></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            