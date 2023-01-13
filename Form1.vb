Public Class Form1
    Public Class Form1
        Private chieudai As Double
        Private chieurong As Double
        Public Property Dientich As Double
        Private Sub Btntinh_Click(sender As Object, e As EventArgs) Handles Btntinh.Click
            chieudai = Val(Txtdai.Text)
            chieurong = Val(Txtrong.Text)
            Dientich = chieudai + chieurong
            TxtDientich.Text = Dientich
        End Sub

        Private Sub Btntiep_Click(sender As Object, e As EventArgs) Handles Btntiep.Click
            Txtdai.Text = ""
            Txtrong.Text = ""
            TxtDientich.Text = ""
        End Sub
    End Class

    Private Sub BtnTinh_Click(sender As Object, e As EventArgs) Handles BtnTinh.Click


    End Sub