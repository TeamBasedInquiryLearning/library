<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:pi="http://pretextbook.org/2020/pretext/internal">
  <xsl:import href="./core/pretext-latex.xsl" />


  <xsl:template match="titlepage-items">
    <xsl:text>[3\baselineskip]&#xa;</xsl:text>
    <xsl:apply-templates select="$bibinfo/author" mode="title-page"/>
    <xsl:text> \\&#xa;</xsl:text>
    <xsl:apply-templates select="$bibinfo/editor" mode="title-page" />
    <xsl:apply-templates select="$bibinfo/credit[title]" mode="title-page" />
  </xsl:template>

  <!--Authors on title page-->
  <xsl:template match="author|editor" mode="title-page">
      <xsl:text> {\Large </xsl:text>
      <xsl:apply-templates select="personname" />
      <xsl:if test="self::editor">
          <xsl:text>, </xsl:text>
          <xsl:apply-templates select="." mode="type-name"/>
      </xsl:if>
      <xsl:text>}  &#xa;</xsl:text>
      <xsl:if test="following-sibling::author">
          <xsl:text> \hspace{0.5in} &#xa;</xsl:text>
      </xsl:if>
  </xsl:template>

  <!--Contributing authors on title page-->
  <xsl:template match="credit" mode="title-page">
    <xsl:text>[3\baselineskip]&#xa;</xsl:text>
    <xsl:text>{\Large </xsl:text>
    <xsl:apply-templates  select="." mode="title-full" />
    <xsl:text>}\\[0.5\baselineskip]&#xa;</xsl:text>
    <xsl:for-each select="author">
        <xsl:text>{\normalsize </xsl:text>
        <xsl:apply-templates select="personname" />
        <xsl:text>}\\</xsl:text>
        <xsl:if test="following-sibling::author">
            <xsl:text>[0.5\baselineskip]&#xa;</xsl:text>
        </xsl:if>
        <xsl:text>&#xa;</xsl:text>
    </xsl:for-each>
  </xsl:template>

  <!--Put definitions in boxes-->
  <xsl:template match="definition" mode="tcb-style">
    <xsl:text>colframe=black!30!white,</xsl:text>
    <xsl:text>coltitle=black,</xsl:text>
    <xsl:text>fonttitle=\bfseries,</xsl:text>
  </xsl:template>

  <!--Tweak display of references-->
  <xsl:template match="xref" mode="latex-page-number">
      <xsl:param name="target"/>

      <xsl:choose>
          <!-- looks bad when bibliographic number gets wrapped in [] -->
          <!-- and the number should suffice on its own               -->
          <xsl:when test="$target/self::biblio"/>
          <!-- and trailing a () for an equation number is overkill -->
          <xsl:when test="$target/self::mrow|$target/self::md"/>
          <!-- and it is really bad for an xref inside a title -->
          <xsl:when test="ancestor::title"/>
          <!-- off by default electronic PDF, -->
          <!-- or on by default for print PDF -->
          <xsl:when test="not($b-pageref)"/>
          <!-- OK, requested and helps, let's add it -->
          <xsl:otherwise>
              <xsl:text> (p.\,\pageref{</xsl:text>
              <xsl:apply-templates select="$target" mode="unique-id"/>
              <xsl:text>})</xsl:text>
          </xsl:otherwise>
      </xsl:choose>
  </xsl:template>

  <!--Controls display of videos and interactives-->
  <xsl:template match="video|interactive[not(static)]" mode="representations">
    <xsl:choose>
        <xsl:when test="$exercise-style = 'static'">
            <!-- panel widths are experimental -->
            <sidebyside margins="7.5% 7.5%" widths="45% 25%" valign="middle" halign="center">
                <!-- copy over @xml:id, which may be in use by -->
                <!-- page-breaking mechanism for LaTeX output  -->
                <xsl:copy-of select="@xml:id"/>
                <!-- A @label could mask an authored @xml:id           -->
                <!-- Note: this may be manufactured by an earlier pass -->
                <xsl:copy-of select="@label"/>
                <xsl:choose>
                    <!-- @preview present, so author provides a static image  -->
                    <!--                                                      -->
                    <!-- "video" is exceptional, we allow for a generic image -->
                    <xsl:when test="self::video and (@preview = 'generic')">
                        <image>
                            <xsl:attribute name="pi:generated">
                                <xsl:text>play-button/play-button.png</xsl:text>
                            </xsl:attribute>
                        </image>
                    </xsl:when>
                    <!--  -->
                    <xsl:when test="@preview">
                        <image>
                            <xsl:attribute name="source">
                                <xsl:value-of select="@preview"/>
                            </xsl:attribute>
                        </image>
                    </xsl:when>
                    <!-- semi-automatic images vary by format     -->
                    <!--                                          -->
                    <!-- interactive: screenshots with playwright -->
                    <!-- video: we scrape YouTube, only           -->
                    <!--        YouTube playlist gets generic     -->
                    <!-- audio: immature                          -->
                    <xsl:when test="self::interactive">
                        <image>
                            <xsl:attribute name="pi:generated">
                                <xsl:text>preview/</xsl:text>
                                <xsl:apply-templates select="." mode="assembly-id"/>
                                <xsl:text>-preview.png</xsl:text>
                            </xsl:attribute>
                        </image>
                    </xsl:when>
                    <!--  -->
                    <xsl:when test="self::video and @youtube">
                        <image>
                            <xsl:attribute name="pi:generated">
                                <xsl:text>youtube/</xsl:text>
                                <xsl:apply-templates select="." mode="assembly-id"/>
                                <xsl:text>.jpg</xsl:text>
                            </xsl:attribute>
                        </image>
                    </xsl:when>
                    <!--  -->
                    <xsl:when test="self::video and @youtubeplaylist">
                        <image>
                            <xsl:attribute name="pi:generated">
                                <xsl:text>play-button/play-button.png</xsl:text>
                            </xsl:attribute>
                        </image>
                    </xsl:when>
                    <!--  -->
                    <xsl:otherwise>
                        <p>BUG: PREVIEW NOT HANDLED</p>
                    </xsl:otherwise>
                </xsl:choose>
                <stack>
                    <!-- Remove bit of code including urls, keep only image of QR code-->
                    <image>
                        <xsl:attribute name="pi:generated">
                            <xsl:text>qrcode/</xsl:text>
                            <xsl:apply-templates select="." mode="assembly-id"/>
                            <xsl:text>.png</xsl:text>
                        </xsl:attribute>
                    </image>
                </stack>
            </sidebyside>
        </xsl:when>
        <xsl:when test="($exercise-style = 'dynamic') or ($exercise-style = 'pg-problems')">
            <!-- duplicate authored content for the non-static conversions -->
            <xsl:copy>
                <xsl:apply-templates select="node()|@*" mode="representations"/>
            </xsl:copy>
        </xsl:when>
    </xsl:choose>
</xsl:template>

</xsl:stylesheet>