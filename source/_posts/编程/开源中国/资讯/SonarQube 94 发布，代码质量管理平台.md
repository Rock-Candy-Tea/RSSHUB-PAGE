
---
title: 'SonarQube 9.4 发布，代码质量管理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5671'
author: 开源中国
comments: false
date: Fri, 08 Apr 2022 15:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5671'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Sonar（SonarQube）是一个开源平台，用于管理源代码的质量。Sonar 不只是一个质量数据报告工具，更是代码质量管理平台。支持的语言包括：Java、PHP、C#、C、Cobol、PL/SQL、Flex 等</span></p> 
<p>SonarQube 在 4 月份发布了最新的 9.4 版本，包含一众改进和 bug 修复：</p> 
<h2>Bug</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-12592" target="_blank">SONAR-12592</a>] - External rules are not removed when no more provided by analyzer</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-13125" target="_blank">SONAR-13125</a>] - Missing information about db migration in sonar.log in console mode when starting SonarQube with jar file</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-13588" target="_blank">SONAR-13588</a>] - Tags defined on external rules are not propagated to external issues</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-14011" target="_blank">SONAR-14011</a>] - Docker not detected in System Information when using AWS ECS</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15974" target="_blank">SONAR-15974</a>] - Escape special characters on Azure DevOps Platform Project onboarding</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15987" target="_blank">SONAR-15987</a>] - Restart should not fail if temp files can't be deleted</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16001" target="_blank">SONAR-16001</a>] - Embedded documentation shows placeholder content for superior edition languages</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16006" target="_blank">SONAR-16006</a>] - "Keep when inactive" button doesn't preserve changed state in UI</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16031" target="_blank">SONAR-16031</a>] - Security fix (SSF-230)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16039" target="_blank">SONAR-16039</a>] - Issues not found on reference branch strategy after migrating from 9.2 to 9.3</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16050" target="_blank">SONAR-16050</a>] - Scanner fails with NPE if user doesn't have permission to analyze project</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16057" target="_blank">SONAR-16057</a>] - Filesystem tests fail with NPE</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16100" target="_blank">SONAR-16100</a>] - Analysis computation errror when a reference branch is used and a file is not under scm control</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16131" target="_blank">SONAR-16131</a>] - CWE titles and descriptions are missing in the security report</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16151" target="_blank">SONAR-16151</a>] - Some file names are wrongly displayed in the issue's page</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16158" target="_blank">SONAR-16158</a>] - Duplicated blocks assigned to the wrong lines of code</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16159" target="_blank">SONAR-16159</a>] - Security fix (SSF-235)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16165" target="_blank">SONAR-16165</a>] - Multiselection of authors is broken in the issue page</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16167" target="_blank">SONAR-16167</a>] - Security fix (SSF-239)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16174" target="_blank">SONAR-16174</a>] - SonarLint icon in PR decoration missing for some DevOps platforms</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16178" target="_blank">SONAR-16178</a>] - Security fix (SSF-241)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16179" target="_blank">SONAR-16179</a>] - Security fix (SSF-240)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16181" target="_blank">SONAR-16181</a>] - Security fix (SSF-227)</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16189" target="_blank">SONAR-16189</a>] - Security fix (SSF-217)</li> 
</ul> 
<h2>New Feature</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15918" target="_blank">SONAR-15918</a>] - Create a new web API endpoint to stream events to SonarLint</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16007" target="_blank">SONAR-16007</a>] - Display hotspots' secondary locations</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16012" target="_blank">SONAR-16012</a>] - Export project license usage from the license page</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16013" target="_blank">SONAR-16013</a>] - Add api endpoint that expose the list of projects with their license usage</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16032" target="_blank">SONAR-16032</a>] - Update Executive Report PDF to reflect Clean As You Code practice</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16101" target="_blank">SONAR-16101</a>] - Track Security Hotspots which represent real risks to fix later</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16123" target="_blank">SONAR-16123</a>] - Display OWASP Top 10 2021 in Security Report</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16192" target="_blank">SONAR-16192</a>] - Improve Terraform analysis: support GCP and detect Traceability problems on Azur</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16208" target="_blank">SONAR-16208</a>] - Improve Python analysis: 8 rules to help developers reduce the complexity of their regular expressions</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16209" target="_blank">SONAR-16209</a>] - Improve JS/TS analysis: support TypeScript 4.6 ; quick fixes support for 30 rules when SonarLint is used in Connected Mode with SQ</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16213" target="_blank">SONAR-16213</a>] - Improve Java analysis: enable Java 18 code parsing</li> 
</ul> 
<h2>Task</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-7496" target="_blank">SONAR-7496</a>] - Drop unused db columns ISSUES.REPORTER, ACTION_PLAN_KEY and ISSUE_ATTRIBUTES</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-12807" target="_blank">SONAR-12807</a>] - Put all ALM icons in a single location</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-13672" target="_blank">SONAR-13672</a>] - Fix Bibucket typo to Bitbucket</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15845" target="_blank">SONAR-15845</a>] - Upgrade H2 database dependency</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15870" target="_blank">SONAR-15870</a>] - Xoo SCM should support relative dates</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15909" target="_blank">SONAR-15909</a>] - Introduce an appState context</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15910" target="_blank">SONAR-15910</a>] - Extract "languages" from redux</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15911" target="_blank">SONAR-15911</a>] - Extract "Metrics" from redux</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15912" target="_blank">SONAR-15912</a>] - Extract "Settings" from redux - part 1: SettingsApp</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15913" target="_blank">SONAR-15913</a>] - Extract "users" from redux</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15914" target="_blank">SONAR-15914</a>] - Clean up redux</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15926" target="_blank">SONAR-15926</a>] - Performance testing of new Server Push API</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15938" target="_blank">SONAR-15938</a>] - Improve code sharing with the license extension</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15962" target="_blank">SONAR-15962</a>] - Drop the "Suggest dependency upgrades" useless Github Action</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15966" target="_blank">SONAR-15966</a>] - Use Spring instead of Pico as dependency injection framework in the scanner-engine</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15977" target="_blank">SONAR-15977</a>] - Fix microsoft jdbc docstring in sonar.properties</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15991" target="_blank">SONAR-15991</a>] - Update frontend dependencies</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15992" target="_blank">SONAR-15992</a>] - Extract "Settings" from redux - part 2: global setting values</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15994" target="_blank">SONAR-15994</a>] - Migrate Sonarqube IOC framework from Pico to Spring</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16005" target="_blank">SONAR-16005</a>] - Remove appState from the Redux store</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16047" target="_blank">SONAR-16047</a>] - Don't start MyBatis in every test</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16055" target="_blank">SONAR-16055</a>] - Upgrade github-action_release to v4</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16073" target="_blank">SONAR-16073</a>] - Add integration test for Projects License Usage export</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16081" target="_blank">SONAR-16081</a>] - Update SelectLegacy component with Select component inside core-extension-governance</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16082" target="_blank">SONAR-16082</a>] - Update SelectLegacy component with Select component inside core-extension-developer-server</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16083" target="_blank">SONAR-16083</a>] - Update SelectLegacy component with Select component inside core-extension-securityreport</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16084" target="_blank">SONAR-16084</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/background-tasks</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16085" target="_blank">SONAR-16085</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/coding-rules</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16086" target="_blank">SONAR-16086</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/component-measures and /issues</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16087" target="_blank">SONAR-16087</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/permissions, /projectBaseline and /projectActivity</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16088" target="_blank">SONAR-16088</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/projectQualityGate and /projectQualityProfiles</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16090" target="_blank">SONAR-16090</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/quality-profiles</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16091" target="_blank">SONAR-16091</a>] - Update SelectLegacy component with Select component inside sonar-web/apps/security-hotspots, /settings and /users</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16092" target="_blank">SONAR-16092</a>] - Update SelectLegacy component with Select component inside sonar-web/app/ and sonar-web/components/</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16113" target="_blank">SONAR-16113</a>] - Expose Select component to extensions using exposeLibraries</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16139" target="_blank">SONAR-16139</a>] - Drop api/users/set_setting and related db table</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16156" target="_blank">SONAR-16156</a>] - Write IT to validate new OWASP Top 10 2021 edition</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16182" target="_blank">SONAR-16182</a>] - Migrate remaining modules from java 8 to java 11</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16199" target="_blank">SONAR-16199</a>] - Correct styling for input in multiselect and other places</li> 
</ul> 
<h2>Improvement</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-10179" target="_blank">SONAR-10179</a>] - Add clear start/stop logs in the different log files</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-10930" target="_blank">SONAR-10930</a>] - Add pagination in WS api/ce/activity</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-11672" target="_blank">SONAR-11672</a>] - Address display of issues reported above file level</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-11718" target="_blank">SONAR-11718</a>] - Increase the number of returned tags in web service</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-11767" target="_blank">SONAR-11767</a>] - Add Server base URL to 'Test Configuration' email</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-12499" target="_blank">SONAR-12499</a>] - Displaying all SonarSource standards in Security Category facets</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-12693" target="_blank">SONAR-12693</a>] - Fix wording in scanner success message log</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-12859" target="_blank">SONAR-12859</a>] - Use new issue icons in pull request decoration</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-13704" target="_blank">SONAR-13704</a>] - Activity of a project is not updated when quality gate is back to green after an update on an issue</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-14721" target="_blank">SONAR-14721</a>] - Do not follow redirects when interacting with GitHub API</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-14722" target="_blank">SONAR-14722</a>] - Do not follow redirects when interacting with Azure DevOps API</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-14723" target="_blank">SONAR-14723</a>] - Do not follow redirects when interacting with Bitbucket Server API</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-14742" target="_blank">SONAR-14742</a>] - Project import from GitHub, Bitbucket and Azure can clash with existing project key</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15554" target="_blank">SONAR-15554</a>] - Update the Permissions text for Quality Profiles</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15695" target="_blank">SONAR-15695</a>] - Better selection behavior for QG admin delegation</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15857" target="_blank">SONAR-15857</a>] - Measure page should support ascending and descending sorting for rating and quality gate</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15919" target="_blank">SONAR-15919</a>] - Add RuleSetChanged event to events streamed to SonarLint</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15921" target="_blank">SONAR-15921</a>] - Add SonarlintClient connected count to system info file, to telemetry and to prometheus monitoring</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15972" target="_blank">SONAR-15972</a>] - Improve responsiveness of the portfolio page</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15975" target="_blank">SONAR-15975</a>] - Change Portfolio overview wording to be more precise</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15979" target="_blank">SONAR-15979</a>] - Make Rating charts in Portfolio Overview Clickable</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15985" target="_blank">SONAR-15985</a>] - Validate user's permission and deactivated/active status before pushing an event</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15989" target="_blank">SONAR-15989</a>] - Fix typo in archived docs warning</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15999" target="_blank">SONAR-15999</a>] - Remove ability to see list of projects as bubble charts</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16008" target="_blank">SONAR-16008</a>] - Improve the hotspot page UX</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16015" target="_blank">SONAR-16015</a>] - Reorganize the license page to better explain how license is being used</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16026" target="_blank">SONAR-16026</a>] - Retry lock on cached analyzers to run multiple scans on the same machine</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16058" target="_blank">SONAR-16058</a>] - Replace parameter 'sinceLeakPeriod' with 'inNewCodePeriod' for 'api/issues/search'</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16059" target="_blank">SONAR-16059</a>] - Add the "Permission" security category</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16064" target="_blank">SONAR-16064</a>] - Add a new API in SensorContext to indicate possibility to skip unchanged files</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16066" target="_blank">SONAR-16066</a>] - Improve executive PDF report</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16069" target="_blank">SONAR-16069</a>] - Scroll to primary location when clicking on the hotspot primary location</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16071" target="_blank">SONAR-16071</a>] - Hotspots UI improvements</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16078" target="_blank">SONAR-16078</a>] - Tag “Removed” displayed on issue is misleading</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16095" target="_blank">SONAR-16095</a>] - Improve the layout of the "Why is this an issue" button</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16096" target="_blank">SONAR-16096</a>] - Create webservices to get and clear scanner plugin cache</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16097" target="_blank">SONAR-16097</a>] - Add plugin cache to the Sensor API</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16098" target="_blank">SONAR-16098</a>] - Improve SonarC# analysis - minor bug fix</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16099" target="_blank">SONAR-16099</a>] - Improve SonarVB analysis - minor bug fix</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16112" target="_blank">SONAR-16112</a>] - Improve Java analysis: minor fix of FPs</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16115" target="_blank">SONAR-16115</a>] - Store plugin's scanner cache in SonarQube</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16119" target="_blank">SONAR-16119</a>] - Enable documentation page for the IaC analyzer</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16124" target="_blank">SONAR-16124</a>] - Add OWASP Top 10 2021 categories to standards.json</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16126" target="_blank">SONAR-16126</a>] - Add CWE Top 25 2021 data to Security Report PDF</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16127" target="_blank">SONAR-16127</a>] - Update the "Authentication" security category</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16128" target="_blank">SONAR-16128</a>] - Update Security Report PDF with OWASP Top 10 2021 data</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16129" target="_blank">SONAR-16129</a>] - Create new facet in Issues search 'OWASP Top 10 - 2021'</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16130" target="_blank">SONAR-16130</a>] - Create new facet in Rules search 'OWASP Top 10 - 2021'</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16141" target="_blank">SONAR-16141</a>] - Security hotspots status and confirmation modal related improvements</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16147" target="_blank">SONAR-16147</a>] - Allow users to assign acknowledged security hotspot</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16152" target="_blank">SONAR-16152</a>] - Do not follow redirects when interacting with Bitbucket Cloud API</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16153" target="_blank">SONAR-16153</a>] - Bitbucket Cloud integration should support custom connection timeout and read timeout</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16155" target="_blank">SONAR-16155</a>] - Allow Security Hotspots to be filtered by OWASP Top 10 2021</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16160" target="_blank">SONAR-16160</a>] - Improve CFamily analysis</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16162" target="_blank">SONAR-16162</a>] - Enable New Code based on "reference branch" with a scanner parameter</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16163" target="_blank">SONAR-16163</a>] - Process reference branch set by the scanner in the CE</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16180" target="_blank">SONAR-16180</a>] - API should validate email address for portfolio reports</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16187" target="_blank">SONAR-16187</a>] - Analysis cache gets cache from different branch when needed</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16188" target="_blank">SONAR-16188</a>] - Deprecate Common Rules and deactivate them for a set of languages</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16196" target="_blank">SONAR-16196</a>] - Improve PHP analysis: improve S1808 and S6328 regexp rules</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16204" target="_blank">SONAR-16204</a>] - Drop SHA1 legacy hash method</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16224" target="_blank">SONAR-16224</a>] - Improve Java Security analysis: better display messages of vulnerabilities involving dependencies</li> 
</ul> 
<h2>Documentation</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-13505" target="_blank">SONAR-13505</a>] - Document how to use SQ Docker image with self-signed certificates</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-13574" target="_blank">SONAR-13574</a>] - Add reference to required Java version in docs</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-14331" target="_blank">SONAR-14331</a>] - Update note on Linux file ownership</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15892" target="_blank">SONAR-15892</a>] - Document the behavior of users/search</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-15976" target="_blank">SONAR-15976</a>] - Mention Microsoft JDBC driver update in the Release notes of 9.3</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16072" target="_blank">SONAR-16072</a>] - Explain License Usage in relation to Lines Of Code</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16125" target="_blank">SONAR-16125</a>] - Update Security Reports page to mention support for OWASP Top 10 2021</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16142" target="_blank">SONAR-16142</a>] - Add Oracle database requirement for max_string_size</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16154" target="_blank">SONAR-16154</a>] - Fix incorrect explanation about VS xml coverage file format for CFamily</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16164" target="_blank">SONAR-16164</a>] - Document new scanner parameter 'sonar.newCode.referenceBranch'</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16186" target="_blank">SONAR-16186</a>] - Add Oracle SQL query for resetting admin password</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16203" target="_blank">SONAR-16203</a>] - Mention Java 17 support in documentation</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fbrowse%2FSONAR-16210" target="_blank">SONAR-16210</a>] - Add instruction to verify which branches to keep before exporting project in Project Move</li> 
</ul> 
<p>同时发布的还有 SonarQube LTS 版本 8.9.8 ，详细信息请看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.sonarsource.com%2Fsecure%2FReleaseNote.jspa%3FprojectId%3D10930%26version%3D17249" target="_blank">这里</a>。 </p>
                                        </div>
                                      
</div>
            